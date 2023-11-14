import os
import shutil
from atlassian import Confluence

URL = os.getenv('ATLASSIAN_URL')
USERNAME = os.getenv('ATLASSIAN_USERNAME')
TOKEN = os.getenv('ATLASSIAN_TOKEN')
SPACE_TO_EXPORT = os.getenv('ATLASSIAN_SPACE_TO_EXPORT')

confluence = Confluence(
    url=URL,
    username=USERNAME,
    password=TOKEN,
    api_version='cloud')

# Get a list of all pages in the space
print('Getting a list of all pages in the space')
pages = confluence.get_all_pages_from_space(SPACE_TO_EXPORT)

# If the exported directory already exists, delete it
if os.path.exists('exported'):
    print('Deleting directory: exported')
    shutil.rmtree('exported')

# Create a directory named "exported" in the current directory if it doesn't already exist
if not os.path.exists('exported'):
    print('Creating directory: exported')
    os.makedirs('exported')

# Export each page
print('Exporting each page to pdf')
for page in pages:
    print(page['id'])
    # Now get the pdf content and write it to file in the directory named "exported"
    pdf = confluence.export_page(page['id'])
    with open('exported/' + page['id'] + '.pdf', 'wb') as f:
        f.write(pdf)
