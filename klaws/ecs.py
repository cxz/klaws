# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from datetime import datetime
import boto3
import urllib.request
import os
import json
from operator import itemgetter
from pprint import pprint

ecs = boto3.client('ecs', region_name='us-east-1')


#need botocore 1.4.37 and boto 1.4.0 for task iam roles.
def run_task(cluster_name, task_name):
    #TODO: pass taskArn in overrides
    r = ecs.run_task(cluster=cluster_name, 
                     taskDefinition=task_name,
                     desiredCount=1,
                     deploymentConfiguration={})    
    pprint(r)
    
def run_task_and_wait(cluster_name, task_name):
    r = ecs.run_task(cluster=cluster_name, taskDefinition=task_name, overrides={
        'containerOverrides': [
        ]
    })
    arn = r['tasks'][0]['taskArn']
    waiter = ecs.get_waiter('tasks_stoped')
    waiter.wait(cluster=cluster_name, tasks=[arn])
    
def shutdown():
    try:
        #delete task
        #delete task definitions
        #terminate instances
        #list_container_instances(cluster=cluster_name)
        #instances = response['containerInstanceArns']
        #describe_container_instances(cluster=cluster_name, containerInstances=instances)
        #terminate_instances(InstanceIds=[ec2_instance['ec2InstanceId']])
        #delete_cluster(cluster=cluster_name)
        print('.')
    except:
        raise                