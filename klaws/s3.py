# -*- coding: utf-8 -*-

import boto3
import botocore

s3 = boto3.resource('s3')

# bucket to use for input & output
# each job will have a key inside this bucket
BUCKET_NAME = '2016-kaggle'

def setup():
    """ Make sure bucket exists, project key is created and acl is ok.
    """
    print
    
def create_project(name):
    if name in list_bucket():
        return
    
    o = get_bucket().put_object(Key=name)
    return o
    

def upload(local_dir, project_name):
    """ Copy from local directory to S3
    
    aws s3 sync local_dir s3://BUCKET_NAME/project_name
    """
    #filename = ""
    #s3.upload_file(filename, BUCKET_NAME, project_name)
    print
    
def download(local_dir, project_name):
    """ Copy from S3 to local directory
    """
    print

def list_bucket():        
    return get_bucket().objects.all()
    
def get_bucket():   
    """ Create bucket if it doesnt exist yet
    """
    bucket = s3.Bucket(BUCKET_NAME)
    try:
        s3.meta.client.head_bucket(Bucket=BUCKET_NAME)
    except botocore.exceptions.ClientError as e:
        if 404 == int(e.response['Error']['Code']):
            return create_bucket()
    return bucket
    
def create_bucket():
    # need to configure ACL
    return s3.create_bucket(Bucket=BUCKET_NAME)
    

def configure():    
    """    
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "s3:ListBucket"
                ],
                "Resource": [
                    "arn:aws:s3:::2016-kaggle"
                ]
            },
            {
                "Effect": "Allow",
                "Action": [
                    "s3:PutObject",
                    "s3:GetObject",
                    "s3:DeleteObject",
                    "s3:ListBucket"
                ],
                "Resource": [
                    "arn:aws:s3:::2016-kaggle/*"
                ]
            }
        ]
    }
    """    
    print

