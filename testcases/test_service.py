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
        
    @classmethod
    def get_dict(cls, obj, fields=None):
        if not fields:
            model = obj.__class__
            fields = [x for x in model._properties.keys() if not x.startswith("_")]
        return {k: getattr(obj, k) for k in fields}

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
        
        for item in Service.list(car):
            if item.replacement_part == "Scam":
                ident = item.key.id()
                break
        service = Service.get(ident, car.key)
        props = {"replacement_part": "BiggestScamOfAllTimes","price_part": 1337, "worked_hrs":45}
        service.update(props)
        
        service = None

        for item in Service.list(car):
            if item.replacement_part == 'BiggestScamOfAllTimes':
                service = item
                        
        self.assertDictEqual(self.get_dict(service, ["price_part", "replacement_part", "worked_hrs"]), props, "error")
        
    
        
