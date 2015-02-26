from testcases.base import BasicTestCase
from practice.model.garage import Garage
from practice.model.car import Car


""" Very simple example how to use the BasicTestCase
"""
class GarageTestCase(BasicTestCase):
    
    def setUP(self):
        ''' This method can be used to import or set up some data needed for every testcase
            
            no need to call super
        '''
        BasicTestCase.setUP(self)
    
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
        self.assertEqual(1, Garage.query().count()) # yay success
        
    def test_twee(self):
        g = Garage()
        g.name = "test1"
        g.brande = "Patat"
        g.note = """ Testing note
        for multi line
        hueaah"""
        g.put()
        
        self.assertEqual(2, Garage.query().count(), "No you suck")
        
        
        for gg in Garage.list("test1"):
            ident = gg.key.id()
        garage = Garage.get(ident)

        c = Car()
        c.name = "blah"
        c.brand = "Patat"
        c.garage = garage.key
        c.put()
        
        ls = Car.listtest(garage)
        print ls
        ls2 = Car.listtest(garage)
        print ls2
        
        self.assertEqual(1, Car.query().count())
        
    def tearDown(self):
        """ tearDown will be called after a testcase
        """
        pass