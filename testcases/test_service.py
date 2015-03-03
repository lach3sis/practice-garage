'''
Created on Mar 2, 2015

@author: michaelroes
'''
from testcases.base.extended import ExtendedTestCase
from practice.model.service import Service
from practice.model.receit import Receit

class Test_service(ExtendedTestCase):

    
    def setUP(self):
        
        ExtendedTestCase.setUP(self)

    '''
    Adding, Editing and Deleting services
    '''
    def test_01(self):
        
        #Adding Service
        garage = self.get_garage()
        car = self.get_car()
        contact = self.get_contact()
        Service.add(car, {"replacement_part": "Scam", "price_part": 137, "worked_hrs": 8})
        self.assertEqual(1, len(Service.list(car)))
        
        #Check if there is a receit created automaticly
        self.assertEqual(1, len(Receit.list(contact, car)))
        
        Service.add(car, {"replacement_part": "BigScam", "price_part": 1337, "worked_hrs": 18})
        self.assertEqual(1, len(Receit.list(contact, car)))
        self.assertEqual(2, len(Service.list(car)))


