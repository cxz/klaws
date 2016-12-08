# -*- coding: utf-8 -*-

from datetime import datetime
import boto3
import urllib.request
import os
import json
from operator import itemgetter
from pprint import pprint

ecs = boto3.client('ecs', region_name='us-east-1')
    
FAMILY_PREFIX = 'klaws-'

def register_batch():
    return register_definition(FAMILY_PREFIX + 'batch', '', "aamaia/kaggle-batch")
    
def register_definition(family_name, role_arn, image):
    """ Register task definition with single container.
    
    :param image from Docker Hub:

    Reference: http://docs.aws.amazon.com/cli/latest/reference/ecs/register-task-definition.html
    """
    r = ecs.register_task_definition(        
        family=family_name,
        taskRoleArn=role_arn,
        containerDefinitions=[{
            "name": family_name + '-1', #not used, because task contains single container
            #"memory": memory,
            #"cpu": cpu,
            #"links": ["mysql"],
            
            #"entryPoint": [],
            #"workingDirectory": "",            
            #"portMappings": [{
            #    "containerPort": 80,
            #    "hostPort": 80
            #}],
            #"environment": [{
            #    "name": "MYSQL_ROOT_PASSWORD",
            #    "value": "password"
            #}],
            #"essential": True
            "image": image
        }]    
    )
    #pprint(r)
    return r['taskDefinition']['taskDefinitionArn']    
    
def deregister_task_definition(arn):
    r = ecs.deregister_task_definition(taskDefinition=arn)
    return r
    
def list_definitions():
    paginator = ecs.get_paginator('list_task_definitions')
    it = paginator.paginate(familyPrefix=FAMILY_PREFIX,
                            PaginationConfig={'MaxItems': 100})
    result = []
    for page in it:
        result.extend(page['taskDefinitionArns'])        
    return result

def describe_definition(arn):
    r = ecs.describe_task_definition(taskDefinition=arn)
    return r
    
    
def list():
    print('.')    
    
def start(task_id, cluster, task_definition):
    r = ecs.start_task(cluster=cluster,
        taskDefinition=task_definition,
        overrides={},
        containerInstances=[],
        startedBy=task_id
        )
    return r
def stop():
    print('')    
    