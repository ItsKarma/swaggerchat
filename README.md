# swaggerchat

ChatGPT over your swagger docs

## Usage

### chatgpt.py

This script will load the files from the `exported/` directory, take your prompt, and use GPT to provide you with a response over your custom data.

```
export OPENAI_API_KEY='YOUR_API_KEY'

python3 chatgpt.py "This is my question over my data"
```

### export_confluence.py

One of the usages of this repo is to ask chat style questions against our confluence space. Often there is so much data that you don't even know the right search terms to use. This script will export your space so the `chatgpt.py` script can index it.

```
export ATLASSIAN_USERNAME='PROBABLY_YOUR_EMAIL_ADDRESS'
export ATLASSIAN_TOKEN='YOUR_TOKEN'
export ATLASSIAN_URL='https://YOUR_WORKSPACE.atlassian.net'
export ATLASSIAN_SPACE_TO_EXPORT='YOUR_SPACE'

python3 export_confluence.py
```
