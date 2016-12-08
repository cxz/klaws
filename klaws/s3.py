# -*- coding: utf-8 -*-

import boto3

s3 = boto3.resource('s3')

def buckets():
    return s3.buckets.all()
    
def get_bucket():    
    return s3.get_bucket('2016-kaggle')

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