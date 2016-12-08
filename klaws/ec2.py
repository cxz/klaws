# -*- coding: utf-8 -*-


from datetime import datetime
import boto3
import urllib.request
import os
import json
from operator import itemgetter
from pprint import pprint

client = boto3.resource('ec2')

def run_instance(cluster_name, instace_type='t2.micro'):
    """ Start instance using ECS AMI and add it to ECS cluster.
    """
    r = client.run_instances(
        # Use the official ECS image
        ImageId="ami-a98cb2c3",
        MinCount=1,
        MaxCount=1,
        InstanceType=instace_type,
        IamInstanceProfile={
            "Name": "ecsInstanceRole"
        },
        UserData="#!/bin/bash \n echo ECS_CLUSTER=" + cluster_name + " >> /etc/ecs/ecs.config"
    )
    pprint(r)    