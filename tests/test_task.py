# -*- coding: utf-8 -*-

#from .context import sample

import unittest
from moto import mock_ecs
from pprint import pprint
import os

import klaws.task as task
import klaws.cluster as cluster


@mock_ecs  
class TaskTestSuite(unittest.TestCase):
    """Basic test cases."""        
    
    CLUSTER_NAME = 'test-cluster'
    
    def setUp(self):
       cluster.create_cluster(TaskTestSuite.CLUSTER_NAME)     
       task.register_batch()        
       
    def tearDown(self):
        cluster.delete_cluster(TaskTestSuite.CLUSTER_NAME)    
            
    def test_task_definition(self):
       
        definitions = task.list_definitions()
        
        arn = task.register_batch()
        self.assertEqual(1 + len(definitions), len(task.list_definitions()))
        
        task.deregister_task_definition(arn)
        self.assertEqual(len(definitions), len(task.list_definitions()))
                        
    def test_task(self):
        #task_id = '1'
        #r = task.start(task_id, TaskTestSuite.CLUSTER_NAME, 'klaws-batch')
        #pprint(r)
        print('')
        
        
if __name__ == '__main__':    
    unittest.main()
    
