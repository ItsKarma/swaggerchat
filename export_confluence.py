import os
from atlassian import Confluence
from tqdm import tqdm

# List of required environment variables
required_env_vars = ['ATLASSIAN_URL', 'ATLASSIAN_USERNAME', 'ATLASSIAN_TOKEN', 'ATLASSIAN_SPACES_TO_EXPORT']

# Dictionary to store the environment variables
env_vars = {}

# Check if all required environment variables are set
for var in required_env_vars:
    if var not in os.environ:
        raise ValueError(f"{var} environment variable is not set")
    else:
        # If the variable is set, store it in the dictionary
        env_vars[var] = os.environ[var]

# Now you can access the environment variables from the dictionary
URL = env_vars['ATLASSIAN_URL']
USERNAME = env_vars['ATLASSIAN_USERNAME']
TOKEN = env_vars['ATLASSIAN_TOKEN']
SPACES_TO_EXPORT = env_vars['ATLASSIAN_SPACES_TO_EXPORT'].split(',')
LOG_LEVEL = os.getenv('LOG_LEVEL', 'warning')


confluence = Confluence(
    url=URL,
    username=USERNAME,
    password=TOKEN,
    api_version='cloud')

# Create a directory named "exported" in the current directory if it doesn't already exist
if not os.path.exists('exported'):
    print('Creating directory: exported')
    os.makedirs('exported')

# Create a directory named "exported/confluence" in the current directory if it doesn't already exist
if not os.path.exists('exported/confluence'):
    print('Creating directory: exported/confluence')
    os.makedirs('exported/confluence')

for SPACE in SPACES_TO_EXPORT:
    # Create a directory for the current space if it doesn't already exist
    if not os.path.exists(f'exported/confluence/{SPACE}'):
        print(f'Creating directory: exported/confluence/{SPACE}')
        os.makedirs(f'exported/confluence/{SPACE}')

    print(f'Exporting each page to pdf from space: {SPACE}')

    start = 0
    limit = 50
    while True:
        pages = confluence.get_all_pages_from_space(SPACE, start=start, limit=limit)
        if not pages:
            break

        for page in tqdm(pages, total=len(pages)):
            if LOG_LEVEL.lower() == 'debug':
                print(page['id'])
            # Now get the pdf content and write it to file in the directory named "exported/confluence/{SPACE}"
            pdf = confluence.export_page(page['id'])
            with open(f'exported/confluence/{SPACE}/{page["id"]}.pdf', 'wb') as f:
                f.write(pdf)

        start += limit
