'''
Created on Mar 2, 2015

@author: michaelroes
'''
from testcases.base.extended import ExtendedTestCase
from practice.model.contact import Contact
import logging

class Test(ExtendedTestCase):


    def setUP(self):
        
        ExtendedTestCase.setUP(self)


    def test_01(self):
        ''' Adding contacts, editing, deleting and retrieving contacts'''
        
        #Adding a new contact
        car = self.get_car()
        Contact.add(car, {"name": "Drac Vladje", "email": "Vladje@dracul.com", "tel_nr": "065461125", "klootfactor": 666, "car": car.key})
        self.assertEqual(1, len(Contact.list(car, "Drac Vladje")))    
        
        #Editing an existing contact
        for item in Contact.list(car, "Drac Vladje"):
            ident = item.key.id()
            props = {"name": "Drac VladiVladderVlad", "email": "Vladje@dracul.com", "tel_nr": "06666-666" }
            contact = Contact.get(ident, car.key)
        contact.update(ident, props)
        self.assertEqual(1, len(Contact.list(car, "Drac VladiVladderVlad")))
        
        #deleting an contact
        contact.delete()
        self.assertEqual(0, len(Contact.list(car)))
        
        
        
        
        
        
        