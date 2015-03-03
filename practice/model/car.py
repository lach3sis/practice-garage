'''
Created on Feb 26, 2015

@author: michaelroes
'''
from google.appengine.ext import ndb
from practice.model.service import Service
from practice.model.receit import Receit
from practice.model.contact import Contact
import time
import logging
from google.appengine.api import memcache


class Car(ndb.Model):
    garage = ndb.KeyProperty(required=True)
    brand = ndb.StringProperty(required=True)
    name = ndb.StringProperty(required=True)
    last_edit = ndb.DateTimeProperty(auto_now=True)
     
    def fill(self,props):
        if 'garage' in props:
            self.garage = props['garage']
        self.brand = props['brand']
        self.name = props['name']
        
    def save(self):
        self.put()
        memcache.delete("cars_%s" % self.garage.urlsafe())
    
    @classmethod
    def update(cls, ident, props):
        c = cls.get(ident=ident)
        c.fill(props=props)
        c.save()
        return c
        
            
    def delete(self):
        self.key.delete()
        memcache.delete("cars_%s" % self.garage.urlsafe())
     
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
        memcache.delete("cars_%s" % garage.key.urlsafe())
        return c
    
    #laat contact zien van huidige auto
    def listcontact(self):
        for contact in Contact.list(self):
            ident = contact.key.id()
        contact = Contact.get(ident, self.key)
        print contact

    def listservices(self):
        services =[]
        for contact in Contact.list(self):
            ident = contact.key.id()
        contact = Contact.get(ident, self.key)
        for x in Service.list(self):
            ident = x.key.id()
            service = Service.get(ident, self.key)
            services.append(service)
        return services



#     @classmethod
#     def listreceit(cls,self):
#         receits =[]
#         if len(Contact.list(self)) > 0 :
#             for contact in Contact.list(self):
#                 ident = contact.key.id()
#             contact = Contact.get(ident, self.key)
#             for r in Receit.list(contact, self):
#                 ident = r.key.id()
#                 receit = Receit.get(ident, contact.key)
#                 receits.append(receit)
#             return receits
#         else:
#             return None
#         return receits
    
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
#         print "this is contact %s" % contact
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
            memcache.delete("receits_%s" % contact.key.urlsafe())   
        elif len(Receit.list(contact, self)) != 0 :
            for receit in Receit.list(contact, self):ident = receit.key.id()
            receit = Receit.get(ident, contact.key, 1)
            receit.total = total
            receit.servicedate = datestamp
            receit.save()
            memcache.delete("receits_%s" % contact.key.urlsafe())
            return total
        else:
            print "Car ERROR!"
        return total

    # Calculation for 1 service
    def calculate(self):
        total = 0.0
        contact = None
        c = Receit.get_by_car(self)
        if c: c.delete()
        c = None
        
        def calc(self, klootfactor=1, worked_hrs=0.0, price_per_hours=0.0, price_part=0.0):
            result = (price_per_hours * worked_hrs)
            if price_part:
                result = result + price_part
            if klootfactor:
                percent = result / 100 * klootfactor
                result = result - percent
            return result  
        
        kf = 1
        for c in Contact.list(self):
            contact = c
            kf = c.klootfactor
        for item in Service.list(car=self):
            total = total + calc(self, kf, item.worked_hrs, self.garage.get().price_per_hours,
                                 item.price_part)

        return Receit.add(self, {'total': total,'servicedate': time.strftime("%x"),
                                 'contact': contact.key if contact else None})

    @classmethod
    def listtest(cls, garage, name=None, limit=20):
        cars = memcache.get("cars_%s" % garage.key.urlsafe())
        if not cars:
            logging.warning("not in memcache")
            q = Car.query(Car.garage == garage.key)
            cars = [ x for x in q]
            memcache.set("cars_%s" % garage.key.urlsafe(), cars)
#         if cars:
#             logging.warning("CACHED!!")
        if limit and len(cars) > limit:
            return cars[:limit]
        return cars

#     @staticmethod
#     def list(garage=None, name=None, limit=20):
#         q = Car.query()
#         if garage:
#             q.filter(Car.garage == garage.key)
#         if name:
#             q.filter(Car.name == name) 
#         if limit:
#             return q.fetch(limit)
#         return [x for x in q.order(Car.name)]
#         # return a list
        

        
