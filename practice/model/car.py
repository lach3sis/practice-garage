'''
Created on Feb 26, 2015

@author: michaelroes
'''
from google.appengine.ext import ndb
from practice.model.service import Service
from practice.model.receit import Receit
import time
import logging
from google.appengine.api import memcache


class Car(ndb.Model):
    garage = ndb.KeyProperty(required=True)
    brand = ndb.StringProperty(required=True)
    name = ndb.StringProperty(required=True)
    last_edit = ndb.DateTimeProperty(auto_now=True)
     
    def fill(self,c):
        if 'garage' in c:
            self.garage = c['garage']
        self.brand = c['brand']
        self.name = c['name']
        
        
             
    def save(self):
        self.put()
        
        
    def delete(self):
        logging.warning("delete function in Car.py")
        self.key.delete()
     
    @staticmethod
    def get(ident):
#         logging.warning("Current ID number : %s" % ident)
        key = ndb.Key("Car", int(ident))
        car = key.get()
        return car

    @classmethod
    def add(cls, garage, params):
        c = Car()
        c.garage = garage.key
        c.fill(params)
        c.put()
        return c
    
    
    def delete_service(self, contact, service):
        Service.delete(service)
        ls = []
        for s in Service.list(self):
            ls.append(s)
        newtotal = self.calculate1(contact, ls)
        print newtotal
#                
    def create_receit(self, contact, data):               
        Receit.add(contact, data)
    
    
    def recalculate(self):
        from practice.model.contact import Contact
        print "%s contacts " % len(Contact.list(self))
        contact = Contact.get_for_car(car=self)
        #contact = Contact.get(ident, self.key)
        print "this is contact %s" % contact
#         contact = Contact.query(Contact.list(self) == self.key)
#         print contact
        


#    Calculation for multiple services
    def calculate1(self, servicelist):
        endTotal = 0.0
        total = 0.0
        klootfactor = 0
        def calc(self, klootfactor=1, worked_hrs=0.0, price_per_hours=0.0, price_part=0.0):
            result = (price_per_hours * worked_hrs)
#             print "%s * %s " % (price_per_hours, worked_hrs) 
            if price_part:
                result = result + price_part
#                 print "+ %s " % price_part
            if klootfactor:
                percent = result / 100 * klootfactor
#                 print ( "%s - %s = " % (result,percent ))
                logging.warning('---- %s ----' % (result-percent))
                return result - percent
             
            return result
        from practice.model.contact import Contact
        for c in Contact.list(self):
            ident = c.key.id()
        contact = Contact.get(ident, self.key)
        klootfactor = contact.klootfactor    
        datestamp = time.strftime("%x")
        for service in servicelist:
            total = total + calc(self, 
                                 klootfactor, 
                                 service.worked_hrs, 
                                 self.garage.get().price_per_hours, 
                                 service.price_part
                                 )
        if len(Receit.list(contact, self)) == 0 :
            self.create_receit(contact, {'total': total,'servicedate': datestamp})
        elif len(Receit.list(contact, self)) != 0 :
            print "Retrieving receit from car !"
            for receit in Receit.list(contact, self):
                ident = receit.key.id()
            receit = Receit.get(ident, contact.key, 1)
            receit.total = total
            receit.servicedate = datestamp
            receit.save()
            return total
        else:
            print "Car ERROR!"
#         for bon in Receit.list(contact):
#             print "Receit info: %s" % bon
        return total
    
       
#     # Calculation for 1 service
#     def calculate(self, service):
#         total = 0.0
#         klootfactor = 0
#         def calc(self, klootfactor=1, worked_hrs=0.0, price_per_hours=0.0, price_part=0.0):
#             result = (price_per_hours * worked_hrs)
#              
#             if price_part:
#                 result = result + price_part
#             if klootfactor:
#                 percent = result / 100 * klootfactor
#                 return result - percent
#              
#             return result
#         from practice.model.contact import Contact
#         for c in Contact.list(self):
#             ident = c.key.id()
#         contact = Contact.get(ident, self.key)
#         klootfactor = contact.klootfactor    
#         datestamp = time.strftime("%x") 
#         total = total + calc(self, klootfactor, service.worked_hrs, self.garage.get().price_per_hours, service.price_part)
# #         self.create_receit(contact, {'total': total,'servicedate': datestamp})
# #         for bon in Receit.list(contact):
# #             print "Receit info: %s" % bon
#         return total

    # Calculation for 1 service
    def calculate(self):
        from practice.model.contact import Contact  
        if (len(Service.list(self)) > 0):
            for s in Service.list(self):
                ident = s.key.id()
            service = Service.get(ident, self.key)
        for c in Contact.list(self):
            ident = c.key.id()
        
        contact = Contact.get(ident, self.key)
        total = 0.0
        klootfactor = contact.klootfactor
      
        def calc(self, klootfactor=1, worked_hrs=0.0, price_per_hours=0.0, price_part=0.0):
            result = (price_per_hours * worked_hrs)
             
            if price_part:
                result = result + price_part
            if klootfactor:
                percent = result / 100 * klootfactor
                return result - percent
             
            return result
#         from practice.model.contact import Contact
#         for c in Contact.list(self):
#             ident = c.key.id()
#         contact = Contact.get(ident, self.key)
#         klootfactor = contact.klootfactor    
        datestamp = time.strftime("%x") 
        total = total + calc(self, klootfactor, service.worked_hrs, self.garage.get().price_per_hours, service.price_part)
        logging.warning("check if there are any receits for this car")
        if len(Receit.list(contact, self)) != 0 :
            for receit in Receit.list(contact, self):
                print "editing receit"
                ident = receit.key.id()
                receit = Receit.get(ident, contact.key)
                receit.total = total
                receit.save()
                
        else:
            self.create_receit(contact, {'total': total,'servicedate': datestamp})
#         for bon in Receit.list(contact):
#             print "Receit info: %s" % bon
        return total
        
#     # Calculate with discount
#     def calculate3(self):
#         total = 0.0
#         klootfactor = 0
#         def calc(self, klootfactor=1, worked_hrs=0.0, price_per_hours=0.0, price_part=0.0):
#             result = (price_per_hours * worked_hrs)
#             
#             if price_part:
#                 result = result + price_part
#             if klootfactor:
#                 percent = result / 100 * klootfactor
#                 return result - percent
#             
#             return result
#         for contact in Contact.list(self):
#             klootfactor = contact.klootfactor
#             
#         for p in Service.list(self):
#             datestamp = time.strftime("%x") 
#             total = total + calc(self, klootfactor, p.worked_hrs, self.garage.get().price_per_hours, p.price_part)
#         for contact in Contact.list(self):
#             tester = self.create_receit(contact, {'total': total,'servicedate': datestamp})
#             for bon in Receit.list(contact):
#                 print "Your last job was :"
#                 print bon
#         return total
#
    @classmethod
    def listtest(cls, garage, name=None, limit=20):
        cars = memcache.get(garage.key.urlsafe())
        if not cars:
            logging.warning("not in memcache")
            q = Car.query(Car.garage == garage.key)
            cars = [ x for x in q]
            memcache.set(garage.key.urlsafe(), cars)
        if limit and len(cars) > limit:
            return cars[:limit]
        return cars

    @staticmethod
    def list(garage=None, name=None, limit=20):
        q = Car.query()
        if garage:
            q.filter(Car.garage == garage.key)
        if name:
            q.filter(Car.name == name) 
        if limit:
            return q.fetch(limit)
        return [x for x in q.order(Car.name)]
        # return a list
        
