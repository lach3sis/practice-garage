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
        '''Fill Car entity with properties
        '''
        if 'garage' in props:
            self.garage = props['garage']
        self.brand = props['brand']
        self.name = props['name']
        
    def save(self):
        '''Save current car entity to datastore
        '''
        self.put()
        memcache.delete("cars_%s" % self.garage.urlsafe())
    
    @classmethod
    def update(cls, ident, props):
        '''Update existing car entity
        '''
        c = cls.get(ident=ident)
        c.fill(props=props)
        c.save()
        return c
        
    def delete(self):
        '''Delete current car
        '''
        self.key.delete()
        memcache.delete("cars_%s" % self.garage.urlsafe())
     
    @staticmethod
    def get(ident):
        '''Retrieve car entity
        '''
        key = ndb.Key("Car", int(ident))
        car = key.get()
        return car
    
    @classmethod
    def add(cls, garage, params):
        '''Add a new car
        '''
        newcar = Car()
        newcar.garage = garage.key
        newcar.fill(params)
        newcar.put()
        memcache.delete("cars_%s" % garage.key.urlsafe())
        return newcar
   
    def add_carcontact(self, props):
        '''Add a contact to current car
        '''
        contact_to_add = Contact(parent = self.key)
        contact_to_add.fill(props)
        contact_to_add.put()
        memcache.delete("contacts_%s" %self.key.urlsafe())
        return contact_to_add
         
    def add_carservice(self, props):
        '''Add a service to current car
        '''
        service_to_add = Service(parent=self.key)
        service_to_add.fill(props)
        service_to_add.save()
        memcache.delete(self.key.urlsafe())
        print "length service list is now %s" % len(Service.list(self))
        self.calculate()
        return service_to_add

    def listcontact(self):
        '''Show contact from current car
        '''
        contact = []
        for c in Contact.list(self):
            ident = c.key.id()
        currentcontact = Contact.get(ident, self.key)
        contact.append(currentcontact)
        return contact

    def listservices(self):
        '''list services from current car
        '''
        services =[]
        for service in Service.list(self):
            services.append(service)
        return services

    @classmethod
    def listreceit(cls,self):
        '''list receits from current car
        '''
        receits =[]
        if len(Receit.list(self.garage.get(), self)) > 0 :
            for receit in Receit.list(self.garage.get(), self):
                receits.append(receit)
            return receits
        else:
            return None
        return receits
    
    def delete_service(self,service):
        '''delete service from car
        '''
        Service.delete(service)
        ls = []
        for s in Service.list(self):
            ls.append(s)
  
        
    def delete_contact(self):
        '''Delete contact from current car
        '''

        for contact in Contact.list(self):
            contact.delete()
            logging.warning("Contact deleted!")
        else:
            logging.warning("Contact not Found!!!")
                     
    def create_receit(self, contact, data):               
        Receit.add(contact, data)
        
    def calculate1(self, servicelist):
        '''Calculate costs for services
        '''
        total = 0.0
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
            logging.error("Car ERROR!")
        return total

    def calculate(self):
        '''(Re)Calculate costs for all services registered by current car
        create receit from result
        '''
        total = 0.0
        contact = None
        c = Receit.get_by_car(self)
        if c: c.delete()
        c = None
        def calc(self, klootfactor=1, worked_hrs=0.0, price_per_hours=0.0, price_part=0.0):
            '''Calculation formula
            '''
            result = (price_per_hours * worked_hrs)
            if price_part:result = result + price_part
            if klootfactor:
                percent = result / 100 * klootfactor
                result = result - percent
            return result  
        kf = 1
        for c in Contact.list(self):
            contact = c
            kf = c.klootfactor
        for item in Service.list(car=self):
            total = total + calc(
                                 self, kf, 
                                 item.worked_hrs, 
                                 self.garage.get().price_per_hours,
                                 item.price_part
                                 )
        return Receit.add(self, {'total': total,
                                 'servicedate': time.strftime("%x"),
                                 'contact': contact.key if contact else None
                                 })

    @classmethod
    def listtest(cls, garage, name=None, limit=20):
        '''List current cars from garage or filter by name
        '''
        cars = memcache.get("cars_%s" % garage.key.urlsafe())
        if not cars:
            q = Car.query(Car.garage == garage.key)
            cars = [ x for x in q]
            memcache.set("cars_%s" % garage.key.urlsafe(), cars)
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