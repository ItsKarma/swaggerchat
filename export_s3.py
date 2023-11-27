import boto3
import os
from tqdm import tqdm

# Specify the AWS profile
aws_profile = os.getenv('AWS_PROFILE', 'default')

# Specify the bucket name
bucket_name = os.getenv('S3_BUCKET_NAME')

# Set up the S3 client
session = boto3.Session(profile_name=aws_profile)
s3 = session.resource('s3')

# Create the local directory if it doesn't exist
if not os.path.exists('exported'):
    os.makedirs('exported')

# List all objects in the S3 bucket
bucket = s3.Bucket(bucket_name)
objects = list(bucket.objects.all())
total_objects = len(objects)

with tqdm(total=total_objects, desc="Downloading", unit='file') as pbar:
    for obj in objects:
        # Create the directory structure in the local system
        if obj.key.endswith('/'):  # Skip directories
            continue
        local_path = 'exported/' + obj.key
        local_dir = os.path.dirname(local_path)
        if not os.path.exists(local_dir):
            os.makedirs(local_dir)
        # Download each file to the local directory
        bucket.download_file(obj.key, local_path)
        pbar.update(1)
