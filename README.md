# swaggerchat

ChatGPT over your swagger docs

## Usage

### Setup

To avoid having to download/install pip packages locally and clutter your filesystem, you can run the following docker command to open a temporary scratch space. You can put all of your environment/secrets in a .env file that will be loaded.

```
docker run -it --rm --env-file .env -v "$(pwd):/app" -v "$HOME/.aws:/root/.aws" -w "/app/" python:3-slim-buster /bin/bash

# upgrade pip
pip install --upgrade pip

# install requirements
pip install -r requirements.txt
```

### chatgpt.py

This script will load the files from the `exported/` directory, take your prompt, and use GPT to provide you with a response over your custom data.

```
export OPENAI_API_KEY='YOUR_API_KEY'
export OPENAI_ORG='YOUR_ORG_ID'

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

### export_s3.py

We keep swagger docs in an s3 bucket, so this script simply exports the files from the s3 bucket to the `exported/` directory. You will first need to create your cli connection to your aws account first.

```
aws sso login --sso-session YOURSESSIONNAME

export S3_BUCKET_NAME='YOURBUCKETNAME'
export AWS_PROFILE='YOURPROFILENAME'

python3 export_s3.py
```
