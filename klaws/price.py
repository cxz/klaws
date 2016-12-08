# -*- coding: utf-8 -*-

from datetime import datetime
import boto3
import urllib.request
import os
import json
from operator import itemgetter

client = boto3.client('ec2')

def history(instace_types):
    data = client.describe_spot_price_history(
        DryRun=False,
        ProductDescriptions = ['Linux/UNIX', 'Linux/UNIX (Amazon VPC)'],
        StartTime=datetime(2016, 12, 7, 20, 59),
        EndTime=datetime(2016, 12, 7, 23, 59),
        InstanceTypes=instace_types
    )
    return data
    
def instance_types():
    filename = '../instances.json'
    if not os.path.isfile(filename):
        urllib.request.urlretrieve('https://raw.githubusercontent.com/powdahound/ec2instances.info/master/www/instances.json', filename)
    with open(filename) as f:
        return json.load(f)
    
def filter_instances(h):
    result = {}
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
        icpu = [k['ECU'], k['vCPU']]
        #max on-demand price across all AZs
        prices = [values.get('linux').get('ondemand') for zone, values in ipricing.items()]
        if len(prices) > 0:
            iprice_max = max(prices)
            iprice_min = min(prices)   
            result[itype] = {'price': [iprice_min, iprice_max], 'mem': imem, 'storage': istorage_size, 'cpu': icpu}            
    return result
        
if __name__ == '__main__':    
    itypes = filter_instances(instance_types())
    ordered = [[k, v['price'][0], v['mem'], v['cpu']] for k, v in itypes.items() if v['mem'] >= 8 and v['mem'] <= 32]
    for k in sorted(ordered, key=lambda x: float(x[1])):
        print(k)
        
    
    selected_types = ['m4.large'] #['t2.large', 'm4.large']
    x = history(selected_types)
    for item in x['SpotPriceHistory']:
        az, itype, desc, price, ts = item['AvailabilityZone'], item['InstanceType'], item['ProductDescription'], item['SpotPrice'], item['Timestamp']
        if itype == 'm4.large':
            print(ts, az, price)

    
    