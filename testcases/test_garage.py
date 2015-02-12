from testcases import BasicTestCase
from src.models.garage import Garage
from src.models.car import Car
import   logging


""" Very simple example how to use the BasicTestCase
"""
class GarageTestCase(BasicTestCase):
    
    def setUP(self):
        ''' This method can be used to import or set up some data needed for every testcase
            
            no need to call super
        '''
        pass
    
    def test_datastore(self):
        ''' start with test_ to get function started
        '''
        g = Garage()
        g.name = "test2222"
        g.brande = "Volvo"
        g.note = """ Testing note
        for multi line
        hueaah"""
        
        g.put()

        for g2 in Garage.query():
            print g2.name
            logging.warning(g2.note)
        self.assertEqual(1, Garage.query().count()) # yay success
    
    def test_this(self):
        
        g = Garage()
        g.name ="sdfa"
        g.brand = "ssf"
        g.note = "asdf"
        
        g.put()
        
        c = Car()
        c.name = "afadf"
        c.brand = "Nissan"
        c.garage = g.key
        c.garage_name = g.name
        logging.warning(c)
        c.put()
        
        logging.warning(g)
        logging.warning(c)
    
    def test_dt(self):
        
        g= Garage()
        g.name="blab"
        g.brand="bugati"
        g.note="rijdniet"
        
        g1= Garage()
        g1.name ="DonEnCor"
        g1.brand = "Nissan"
        g1.note = "testnote"
        
        g.put()
        g1.put()
        
        
        for g2 in Garage.query():
            print g2.name
        self.assertEqual(3, Garage.query().count())
        
    def tearDown(self):
        """ tearDown will be called after a testcase
        """
        pass