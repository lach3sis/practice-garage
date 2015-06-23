import os
import unittest2
from google.appengine.api import memcache
from google.appengine.ext import testbed
from google.appengine.ext.testbed import DATASTORE_SERVICE_NAME
from google.appengine.datastore import datastore_stub_util
import logging

from google.appengine.api import apiproxy_stub_map,datastore_file_stub

from practice.model.garage import Garage


class BasicTestCase(unittest2.TestCase):
    
    def setUP(self):
        ''' Override this method
        '''
        #self.set_up_testbed()
        
    @classmethod
    def setUpClass(cls):
        cls.set_up_testbed()
        
    @classmethod
    def set_up_testbed(cls):
        print "initializing Testbed"
        # First, create an instance of the Testbed class.
        cls.testbed = testbed.Testbed()
        # Then activate the testbed, which prepares the service stubs for use.
        cls.testbed.activate()
        # Create a consistency policy that will simulate the High Replication consistency model.
        cls.policy = datastore_stub_util.PseudoRandomHRConsistencyPolicy(probability=0)
        # Initialize the datastore stub with this policy.
        cls.testbed.init_datastore_v3_stub(enable=False, consistency_policy=cls.policy)
        cls.testbed.init_memcache_stub()

        logging.warning("Testbed Ready!")
        cls.testbed.init_datastore_v3_stub()
    
    @classmethod
    def load_datastore(cls, datastore_image=None):
        """ Loads a datastore with test data
        """
        cls.log("Loading datastore image: %s" % datastore_image)
        if not datastore_image:
            datastore_file = '/dev/null'
        else:
            datastore_file = os.path.join(os.path.dirname(__file__), '../testdata/' + datastore_image)

        cls.testbed.init_datastore_v3_stub(enable=False)
        cls.testbed.init_datastore_v3_stub(datastore_file=datastore_file, save_changes=False)
    
    @classmethod
    def tearDownClass(cls):
        cls.testbed.deactivate()
