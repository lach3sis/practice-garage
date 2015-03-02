'''
Created on Mar 2, 2015

@author: michaelroes
'''
from testcases.base import BasicTestCase
from practice.model.garage import Garage
from practice.model.car import Car
from practice.model.contact import Contact
from practice.model.service import Service
from practice.model.receit import Receit 



class Test_case1(BasicTestCase):


    def setUP(self):
        ''' This method can be used to import or set up some data needed for every testcase
            
            no need to call super
        '''
        BasicTestCase.setUP(self)

    #adding Garage entity
    def test_01(self):
        Garage.add({"name": "TurboTune", "brand": "Porsche", "price_per_hours": 11, "note": "Wij zijn Dicht!"})
        
        self.assertEqual(1, len(Garage.list()), "No you suck")
        
        #editing Garage
    def test_02(self):
        
        for g in Garage.list("TurboTune"): ident = g.key.id()
        garage = Garage.get(ident)
        props = {"name": "TurboWave", "brand": "RUF"}
        
        garage.update(garage.key.id(), props)
        self.assertEqual(1, len(Garage.list("TurboWave")))
        
        
        #deleting garage
    def test_03(self):
        
        for g in Garage.list("TurboWave"):
            ident = g.key.id()
        garage = Garage.get(ident)
        Garage.delete(garage)
        
        self.assertEqual(0, len(Garage.list()))
        
        #adding Cars
    def test_04(self):
        Garage.add({"name": "TurboCannon", "brand": "Porsche", "price_per_hours": 11, "note": "Wij zijn Dicht!"})
        
        for gg in Garage.list("TurboCannon"):ident = gg.key.id()
        garage = Garage.get(ident)
        
        Car.add(garage, {"name": "911 Carera", "brand": "Porsche", "garage": garage.key})
      
        self.assertEqual(1, len(Car.listtest(garage)))
    
        #editing Car
    def test_05(self):
        
        for gg in Garage.list("TurboCannon"):ident = gg.key.id()
        garage = Garage.get(ident)
        
        for c in Car.listtest(garage, "911 Carera"): ident = c.key.id()
        car = Car.get(ident)
        
        props = {"name": "Champion", "brand": "RUF"}
        Car.update(car.key.id(), props)

        self.assertEqual(1, len(Car.listtest(garage,"Champion")))
        
        #deleting car
    def test_06(self):
        
        for gg in Garage.list("TurboCannon"):ident = gg.key.id()
        garage = Garage.get(ident)
        
        for c in Car.listtest(garage, "Champion"): ident = c.key.id()
        car = Car.get(ident)
        
        Car.delete(car)
         
        self.assertEqual(0, len(Car.listtest(garage,"Champion")))      
    
    def test_07(self):
        
        Garage.add({"name": "SlowTune", "brand": "Volkswagen", "price_per_hours": 15})
        
        self.assertEqual(1, len(Garage.list("SlowTune")))
        
        for gg in Garage.list("SlowTune"): ident = gg.key.id()
        garage = Garage.get(ident)
        
        Car.add(garage, {"name": "544TRX", "brand": "Volkswagen", "garage": garage.key})
        
        self.assertEqual(1, len(Car.listtest(garage, name="544TRX")))
            
    def test_08(self):
        
        for g in Garage.list("SlowTune"): ident = g.key.id()
        garage = Garage.get(ident)
        
        Car.add(garage, {"name": "FastName", "brand": "Volkswagen", "garage": garage.key})
        self.assertEqual(2, len(Car.listtest(garage)))
        
        Car.add(garage, {"name": "SlowJoe", "brand": "Volkswagen", "garage": garage.key})
        self.assertEqual(3, len(Car.listtest(garage)))
        
        Car.add(garage, {"name": "Speedy", "brand": "Volkswagen", "garage": garage.key})
        self.assertEqual(4, len(Car.listtest(garage)))
        
        Car.add(garage, {"name": "Monster", "brand": "Volkswagen", "garage": garage.key})
        self.assertEqual(5, len(Car.listtest(garage)))
        
        for c in Car.listtest(garage, "SlowJoe"):
            ident = c.key.id()
        car = Car.get(ident)
        
        Car.delete(car)
        
        self.assertEqual(4, len(Car.listtest(garage)))
        
    def test_09(self):
        pass
    
        