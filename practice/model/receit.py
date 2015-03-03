from google.appengine.ext import ndb
from google.appengine.api import memcache
import logging

class Receit(ndb.Model):
    garage = ndb.KeyProperty(kind="Garage")
    car = ndb.KeyProperty(kind="Car", required=True)

    servicedate = ndb.StringProperty()
    total = ndb.FloatProperty()
    
    contact = ndb.KeyProperty("Contact")
    
    
    def fill(self, param):
        if 'servicedate' in param:
            self.servicedate = param['servicedate']
        if 'total' in param:
            self.total = param['total']
        if "car" in param:
            self.car = param['car']
        if "contact" in param:
            self.contact = param["contact"]
        
    def save(self):
        self.put()
       
        #Delete entity by key
    def delete(self):
        self.key.delete()
    
    @classmethod
    def add(cls, car, props):
        r = Receit()
        props["garage"] = car.garage
        props["car"] = car.key
        r.fill(props)
        r.save()
        return r

    @classmethod
    def get(cls, ident):
        key = ndb.Key("Receit", int(ident))
        receit = key.get()
        return receit
    
    @classmethod
    def get_by_car(cls, car):
        return cls.query().filter(cls.car==car.key).get()
    
    @classmethod
    def list(cls, garage=None, car=None, contact=None, limit=20):

        q = Receit.query()
        if car:
            q = q.filter(Receit.car == car.key)
            return [q.get()]
        elif contact:
            q = q.filter(Receit.contact == contact.key)
            return [q.get()]
        elif garage:
            q = q.filter(Receit.garage == garage.key)
        if limit:
            return q.fetch(limit)
        return [x for x in q]
    
    @classmethod
    def mem(cls,contact):
        receits = memcache.get("receits_%s" % contact.key.urlsafe())
        return receits
    
        