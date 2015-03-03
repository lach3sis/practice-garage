from google.appengine.ext import ndb
from google.appengine.api import memcache
import logging


class Contact(ndb.Model):
    name = ndb.StringProperty(required = True)
    email = ndb.StringProperty(required = False)
    tel_nr = ndb.StringProperty()
    klootfactor = ndb.IntegerProperty()
    car = ndb.KeyProperty() 
    

    
    def fill(self, param):
        if 'name' in param:
            self.name = param['name']
        if 'email' in param:
            self.email = param['email']
        if 'tel_nr' in param:
            self.tel_nr = param['tel_nr']
        if 'klootfactor' in param:
            self.klootfactor = param['klootfactor']
        if 'car' in param:
            self.car = param['car']
            
            
        
    def save(self):
        self.put()
        
        #Delete entity by key
    def delete(self):
        self.key.delete()
        memcache.delete("contacts_%s" %self.key.parent().urlsafe())
    
    #Add a new contact
    @classmethod
    def add(cls, car, g):
        c = Contact(parent = car.key)
        c.fill(g)
        c.put()
        memcache.delete("contacts_%s" %car.key.urlsafe())
        return c

    
    #update an existing contact

    def update(self, ident, props):
        c = self.get(ident, self.key.parent())
        c.fill(props)
        c.save()
        return c
    
    
#     @staticmethod
#     def get(ident, garagekey, limit=20):
#         key = ndb.Key("Contact", int(ident), parent=garagekey)
#         contact = key.get()
#         return contact

    @staticmethod
    def get(ident, carkey):
        key = ndb.Key("Contact", int(ident), parent=carkey)
        contact = key.get()
        return contact
    
    @classmethod
    def get_for_car(cls, car):
        if not car:
            logging.warning("NO CAR!")
            return
        cs = cls.list(car=car)
        if(cs):
            return cs[0]
    
    @classmethod
    def list(cls, car, name=None, limit=20):
        contacts = memcache.get("contacts_%s" %car.key.urlsafe())
        if not contacts:
            logging.warning("not in memcache")
            q = Contact.query(ancestor=car.key)
            contacts = [ x for x in q]
            memcache.set("contacts_%s" %car.key.urlsafe(), contacts)
        if limit and len(contacts) > limit:
            return contacts[:limit]
        return contacts
        

    