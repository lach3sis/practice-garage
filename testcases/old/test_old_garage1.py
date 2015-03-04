from testcases.base.extended import ExtendedTestCase
from practice.model.garage import Garage
from practice.model.car import Car
from practice.model.contact import Contact
from practice.model.service import Service
from practice.model.receit import Receit 
""" Very simple example how to use the BasicTestCase
"""
class GarageTestCase(ExtendedTestCase):
    
    def setUP(self):
        ''' This method can be used to import or set up some data needed for every testcase
            
            no need to call super
        '''
        ExtendedTestCase.setUP(self)
    
    def test_01(self):
        ''' start with test_ to get function started
        '''
        garage = self.get_garage()
        
        self.assertEqual(1, Garage.query().count()) # yay success
        
    def test_02(self):
        
        garage = self.get_garage()
        Garage.update(garage.key.id(), {"name": "test1", "brand": "Patat", "price_per_hours": 15 })

        
        self.assertEqual(1, Garage.query().count(), "No you suck")
        
#         
#         for gg in Garage.list("test1"):
#             ident = gg.key.id()
#         garage = Garage.get(ident)
# 
#         c = Car()
#         c.name = "blah"
#         c.brand = "Patat"
#         c.garage = garage.key
#         c.put()
#         
#         ls = Car.listtest(garage)
#         print ls
#         ls2 = Car.listtest(garage)
#         print ls2
#         
#         self.assertEqual(1, Car.query().count())
        
    def test_03(self):
        

        garage = self.get_garage()
        car = self.get_car()
        
        Contact.add(car, {"name": "Tom Sawyer", "email": "Tom@sawyer.com", "tel_nr": "065461125", "klootfactor": 7, "car": car.key})
        Service.add(car, {"replacement_part": "Oil", "price_part": 45, "worked_hrs": 3})
        Service.add(car, {"replacement_part": "Cleaning", "price_part": 15, "worked_hrs": 2})
        Service.add(car, {"replacement_part": "Tuning", "price_part": 120, "worked_hrs": 5})
        
#         print len(Service.list(car))
#         print Service.list(car, "Cleaning")
        Service.add(car, {"replacement_part": "Cleaning", "price_part": 654, "worked_hrs": 92})
        
        servicelist = []
        counter = 0
        
        print len(Service.list(car))
        
        while counter < 15:
            s = Service(parent=car.key)
            s.replacement_part = "Tunejob :%s" % counter
            s.price_part = (5+counter)
            s.worked_hrs = (1+counter)
            servicelist.append(s)
            counter = counter + 1
        Service.multiadd(car, servicelist)
        
        for c in Contact.list(car):
            ident = c.key.id()
        contact = Contact.get(ident, car.key)
        
#         car.calculate1(servicelist)
        
        for xx in Receit.list(contact, car):
            ident = xx.key.id()
            receit = Receit.get(ident, contact.key)
        print receit.total
        print len(Receit.list(contact, car))
         
         
#     def test_04(self):
#         
#         garage = self.get_garage()
#         car = self.get_car()
#         
#         print car.listreceit(car)
#         
#         

    def tearDown(self):
        """ tearDown will be called after a testcase
        """
        pass