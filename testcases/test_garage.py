'''
Created on Mar 2, 2015

@author: michaelroes
'''
from testcases.base import BasicTestCase
from practice.model.garage import Garage
from practice.model.car import Car
from testcases.base import ExtendedTestCase


class Test_case1(BasicTestCase):


    def setUP(self):
        ''' This method can be used to import or set up some data needed for every testcase
            
            no need to call super
        '''
        BasicTestCase.setUP(self)

        ''' 
        Adding, Editing, Deleting Garages
        '''    
    def test_01(self):
        Garage.add({"name": "TurboTune", "brand": "Porsche", "price_per_hours": 11, "note": "Wij zijn Dicht!"})
        self.assertEqual(1, len(Garage.list()), "No you suck")

        
        #editing Garage
        for g in  Garage.list("TurboTune"):
            ident = g.key.id()
        garage = Garage.get(ident)
        print garage
        props = {"name": "TurboWave", "brand": "RUF"}
        Garage.update(garage.key.id(), props)
        self.assertEqual(1, len(Garage.list("TurboWave")))
            
        #deleting garage      
        Garage.delete(garage)
        self.assertEqual(0, len(Garage.list()))            

    def test_02(self):
        pass

        

    def test_03(self):
        pass
        
    '''
    Adding, Editing and deleting cars
    '''
    def test_04(self):
        pass
    def test_05(self):
        pass

    def test_06(self):
        pass
    
    def test_07(self):
        pass
           
    def test_08(self):
        pass
#         
#         for g in Garage.list("SlowTune"): ident = g.key.id()
#         garage = Garage.get(ident)
#         
#         Car.add(garage, {"name": "FastName", "brand": "Volkswagen", "garage": garage.key})
#         self.assertEqual(2, len(Car.listtest(garage)))
#         
#         Car.add(garage, {"name": "SlowJoe", "brand": "Volkswagen", "garage": garage.key})
#         self.assertEqual(3, len(Car.listtest(garage)))
#         
#         Car.add(garage, {"name": "Speedy", "brand": "Volkswagen", "garage": garage.key})
#         self.assertEqual(4, len(Car.listtest(garage)))
#         
#         Car.add(garage, {"name": "Monster", "brand": "Volkswagen", "garage": garage.key})
#         self.assertEqual(5, len(Car.listtest(garage)))
#         
#         for c in Car.listtest(garage, "SlowJoe"):
#             ident = c.key.id()
#         car = Car.get(ident)
#         
#         Car.delete(car)
#         
#         self.assertEqual(4, len(Car.listtest(garage)))
        
    def test_09(self):
        pass
    
        