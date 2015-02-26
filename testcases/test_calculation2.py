""" Very simple example how to use the BasicTestCase
"""

from src.models.car import Car
from src.models.contact import Contact
from src.models.garage import Garage
from src.models.repaircar import Service
from testcases import BasicTestCase


class GarageTestCase(BasicTestCase):
    
    def setUP(self):
        ''' This method can be used to import or set up some data needed for every testcase
            
            no need to call super
        '''
        pass

        
        
    def create_garage(self, data):
        return Garage.add(data)
    
    def create_car(self, garage, data):
        return Car.add(garage, data)
    
    def create_service(self, car, data):
        Service.add(car, data)
    
    def create_contact(self, car, data):
        Contact.add(car, data)
        
    def calc(self, garage, car, data, result):
        k = self.create_garage(garage)
        print k
        h = self.create_car(k, car)
        for i in data:
            self.create_service(h, i)
        self.assertEqual(result, h.calculate3())
        
    def test_01(self):
        
        g = {"name": "GarageDubi", "brand": "Porsche", "price_per_hours": 12}
        c = {"name": "FastName", "brand": "Nissan"}
        list1 = [{"replacement_part": 'Windows', "price_part": 50, "worked_hrs":5},
                 {"replacement_part": 'Ashtray', "price_part": 50, "worked_hrs":4},
                 {"replacement_part": 'Ashtray', "price_part": 100, "worked_hrs":1}]
        
        self.calc(g, c, list1, 320)

        g = {"name": "ljllkj", "brand": "Porsche", "price_per_hours": 125}
        c = {"name": "FastName", "brand": "Nissan"}
        list1 = [{"replacement_part": 'Windows', "price_part": 550, "worked_hrs":5},
                 {"replacement_part": 'Ashtray', "price_part": 450, "worked_hrs":4},
                 {"replacement_part": 'Ashtray', "price_part": 100, "worked_hrs":1}]        
        
        self.calc(g, c, list1, 2350)
        
        g = {"name": "oiuoiu", "brand": "Porsche", "price_per_hours": 25}
        c = {"name": "FastName", "brand": "Nissan"}
        list1 = [{"replacement_part": 'Windows', "price_part": 550, "worked_hrs":5},
                 {"replacement_part": 'Ashtray', "price_part": 350, "worked_hrs":5},
                 {"replacement_part": 'Ashtray', "price_part": 100, "worked_hrs":10}]
        
        self.calc(g, c, list1, 1500)
        
        g = {"name": "oiuoiu", "brand": "Porsche", "price_per_hours": 5}
        c = {"name": "FastName", "brand": "Nissan"}
        list1 = [{"replacement_part": 'Windows', "price_part": 550, "worked_hrs":10},
                 {"replacement_part": 'Ashtray', "price_part": 350, "worked_hrs":10},
                 {"replacement_part": 'Ashtray', "price_part": 100, "worked_hrs":10}]        
              
        self.calc(g, c, list1, 1150)

    def tearDown(self):
        """ tearDown will be called after a testcase
        """
        pass