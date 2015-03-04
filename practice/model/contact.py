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
        '''Fill Contact entity with properties
        '''
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
        

    def delete(self):
        '''Delete current contact
        '''
        self.key.delete()
        memcache.delete("contacts_%s" %self.key.parent().urlsafe())
    
    
    @classmethod
    def add(cls, car, g):
        '''Add a new contact
        '''
        c = Contact(parent = car.key)
        c.fill(g)
        c.put()
        memcache.delete("contacts_%s" %car.key.urlsafe())
        return c

    def update(self, ident, props):
        '''Update an existing contact
        '''
        c = self.get(ident, self.key.parent())
        c.fill(props)
        c.save()
        return c
    
    @staticmethod
    def get(ident, carkey):
        '''Retrieve Contact entity by car key
        '''
        key = ndb.Key("Contact", int(ident), parent=carkey)
        contact = key.get()
        return contact
    
    @classmethod
    def get_for_car(cls, car):
        '''List car by contact
        '''
        if not car:
            logging.warning("NO CAR!")
            return
        cs = cls.list(car=car)
        if(cs):
            return cs[0]
    
    @classmethod
    def list(cls, car, name=None, limit=20):
        '''List all cars or search by name
        '''
        contacts = memcache.get("contacts_%s" %car.key.urlsafe())
        if not contacts:
            q = Contact.query(ancestor=car.key)
            contacts = [ x for x in q]
            memcache.set("contacts_%s" %car.key.urlsafe(), contacts)
        if limit and len(contacts) > limit:
            return contacts[:limit]
        return contacts   