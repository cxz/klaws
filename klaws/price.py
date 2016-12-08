# -*- coding: utf-8 -*-

from datetime import datetime
import boto3
import urllib.request
import os
import json

client = boto3.client('ec2')

def history():
    data = client.describe_spot_price_history(
        DryRun=False,
        StartTime=datetime(2016, 12, 1),
        EndTime=datetime(2016, 12, 6),
        #InstanceTypes=['t1.micro|t2.nano']
    )
    return data
    
def instance_types():
    filename = '../instances.json'
    if not os.path.isfile(filename):
        urllib.request.urlretrieve('https://raw.githubusercontent.com/powdahound/ec2instances.info/master/www/instances.json', filename)
    with open(filename) as f:
        return json.load(f)
    
def filter_instances(h):
    for k in h:
        itype = k['instance_type']
        #iname = k['pretty_name']
        ipricing = k['pricing']
        istorage = k['storage']
        if istorage is None:
            istorage_size = None
        else:
            istorage_size = istorage['size']
        imem = k['memory']
        #max on-demand price across all AZs
        prices = [values.get('linux').get('ondemand') for zone, values in ipricing.items()]
        if len(prices) > 0:
            iprice_max = max(prices)
            iprice_min = min(prices)   
            print(','.join([itype, str(iprice_min), str(iprice_max), str(imem), str(istorage_size)]))
        
if __name__ == '__main__':
    types = instance_types()
    filter_instances(types)
    #x = history()
    