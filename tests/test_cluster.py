# -*- coding: utf-8 -*-

#from .context import sample

import unittest
from moto import mock_ecs

import klaws.cluster as k


@mock_ecs    
class ClusterTestSuite(unittest.TestCase):
    """Basic test cases."""        
    
        
    def test_cluster(self):
        cluster_name = 'test-1'
        arn = k.create_cluster(cluster_name)
                
        clusters = k.describe_clusters([arn])
        self.assertEqual(1, len(clusters))
                
        k.delete_cluster(arn)        
        self.assertEqual(0, len(k.list_clusters()))
                
            
if __name__ == '__main__':    
    #httpretty doesnt work with proxy 
    #del os.environ['HTTP_PROXY'] 
    #del os.environ['http_proxy']
    #del os.environ['https_proxy']
    #del os.environ['HTTP_PROXY']    
    unittest.main()
    
