'''
Created on Mar 2, 2015

@author: michaelroes
'''
from testcases.base.base import BasicTestCase
from testcases.base.extended import ExtendedTestCase
from practice.model.car import Car
import logging


class Test_car(ExtendedTestCase):

    def setUP(self):
        
        ExtendedTestCase.setUP(self)

    def test_01(self):
        ''' Adding cars, editing, deleting and retrieving cars
        '''
        
        #Add a car
        garage = self.get_garage() 
        Car.add(garage, {"name": "Lightning", "brand": "Bugatti", "garage": garage.key})

        self.assertEqual(1, len(Car.listtest(garage, "Lightning")))
        Car.add(garage, {"name": "Vulcano", "brand": "Porsche", "garage": garage.key})
        self.assertEqual(2, len(Car.listtest(garage)))
        
        #Update a car
        for c in Car.listtest(garage):
            ident = c.key.id()
        car = Car.get(ident)
        props = {"name": "Tsunami", "brand": "Saab" }
        Car.update(ident, props)      
        self.assertEqual("Tsunami", car.name, "names do not correspond")
        
        #Deleting a car
        Car.delete(car)
        self.assertEqual(1, len(Car.listtest(garage)), "there is either more or less than 1 car left")

                 
        