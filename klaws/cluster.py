# -*- coding: utf-8 -*-

import boto3

ecs = boto3.client('ecs', region_name='us-east-1')

def list_clusters():    
    paginator = ecs.get_paginator('list_clusters')
    it = paginator.paginate(PaginationConfig={'MaxItems': 100})
    result = []
    for page in it:
        result.extend(page['clusterArns'])        
    return result
    
def create_cluster(name):
    r = ecs.create_cluster(clusterName=name)
    return r['cluster']['clusterArn']
    
def delete_cluster(name):
    ecs.delete_cluster(cluster=name)
    
    
def describe_clusters(names):
    r = ecs.describe_clusters(clusters=names)    
    assert 0 == len(r['failures'])
    return r['clusters']
