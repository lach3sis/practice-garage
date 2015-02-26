""" Very simple example how to use the BasicTestCase
"""

import logging

from src.models.car import Car
from src.models.garage import Garage
from src.models.repaircar import Service
from testcases import BasicTestCase


class GarageTestCase(BasicTestCase):
    
    services = {"service1" : {"replacement_part": "pa",
                              "price_part": 40.2,
                              "worked_hrs": 5}}
    
    my_dict = [{'name': "a",
               'brand': "ab",
               'cars': [{'name': "tootoot1",
                         "brand": "test",
                         'services': [services["service1"]]}
                        ]
                }]
    
    def setUP(self):
        ''' This method can be used to import or set up some data needed for every testcase
            
            no need to call super
        '''
        pass
    
#     def test_datastore(self):
#         ''' start with test_ to get function started
#         '''
#         g = Garage()
#         g.name = "test2222"
#         g.brande = "Volvo"
#         g.note = """ Testing note
#         for multi line
#         hueaah"""
#         
#         g.put()
# 
#         for g2 in Garage.query():
#             print g2.name
#             logging.warning(g2.note)
#         self.assertEqual(1, Garage.query().count()) # yay success
#     
#     def test_this(self):
#         
#         g = Garage()
#         g.name ="sdfa"
#         g.brand = "ssf"
#         g.note = "asdf"
#         
#         g.put()
#         
#         c = Car()
#         c.name = "afadf"
#         c.brand = "Nissan"
#         c.garage = g.key
#         c.garage_name = g.name
#         logging.warning(c)
#         c.put()
#         
#         logging.warning(c.garage)
#         logging.warning(g)
#         logging.warning(c)
#     
#     def test_dt(self):
#         
#         g= Garage()
#         g.name="blab"
#         g.brand="bugati"
#         g.note="rijdniet"
#         
#         g1= Garage()
#         g1.name ="DonEnCor"
#         g1.brand = "Nissan"
#         g1.note = "testnote"
#         
#         g.put()
#         g1.put()
#         
#         
#         for g2 in Garage.query():
#             print g2.name
#         self.assertEqual(3, Garage.query().count())
        
    def test_example(self):
        print "---------- test example -----------"
        for g in self.my_dict:
            ga = Garage()
            ga.brand = g["brand"]
            ga.name = g["name"]
            ga.save()
            for c in g["cars"]:
                car = Car.add(ga, c)
                for s in c["services"]:
                    Service.add(car, s)
                    
        for g in Garage.query():
            print "Name: " + g.name
            print "----- Cars -------"
            for car in Car.list(g):
                print "Name: " + car.name
                print "---services -----"
                for service in Service.list(car):
                    print service.replacement_part + " - " + str(service.price_part) + " - " + str(service.worked_hrs)
                
            
        
    def tearDown(self):
        """ tearDown will be called after a testcase
        """
        pass