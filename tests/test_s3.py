# -*- coding: utf-8 -*-

#from .context import sample

import unittest
from moto import mock_s3
from pprint import pprint
import os
import klaws.s3 as s3


@mock_s3  
class S3TestSuite(unittest.TestCase):
    """Basic test cases."""        
            
    def setUp(self):
       #cluster.create_cluster(TaskTestSuite.CLUSTER_NAME)     
       #task.register_batch()        
       print
       
    def tearDown(self):
        #cluster.delete_cluster(TaskTestSuite.CLUSTER_NAME)    
        print
            
                        
    def test_list_bucket(self):
        s3.list_bucket()        
        
    def test_create_project(self):
        s3.create_project('tmp1')
        
        
if __name__ == '__main__':    
    unittest.main()
    
