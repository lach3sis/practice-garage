from google.appengine.ext import ndb
from google.appengine.api import memcache
import logging

class Receit(ndb.Model):
    servicedate = ndb.StringProperty(required = False)
    total = ndb.FloatProperty()
    car = ndb.KeyProperty(indexed = True)
    service = ndb.KeyProperty(indexed = True)
    
    
    def fill(self, param):
        if 'servicedate' in param:
            self.servicedate = param['servicedate']
        if 'total' in param:
            self.total = param['total']
        if "car" in param:
            self.car = param['car']
        if "service" in param:
            self.service = param['service']
        
    def save(self):
        self.put()
        memcache.delete("receits_%s" % self.key.parent().urlsafe())
       
        #Delete entity by key
    def delete(self):
        self.key.delete()
        memcache.delete("receits_%s" % self.key.parent().urlsafe())
    
    @classmethod
    def add(cls, contact, g):
        r = Receit(parent = contact.key)
        r.fill(g)
        r.put()
        memcache.delete("receits_%s" % contact.key.urlsafe())
        return r
    
#     @staticmethod
#     def get(ident, garagekey, limit=20):
#         key = ndb.Key("Contact", int(ident), parent=garagekey)
#         contact = key.get()
#         return contact


    @staticmethod
    def get(ident, contactkey, limit=20):
        key = ndb.Key("Receit", int(ident), parent=contactkey)
        receit = key.get()
        return receit
    
    @classmethod
    def list(cls, contact, car=None, service=None, limit=20):
        receits = memcache.get(contact.key.urlsafe())
        if not receits:
            logging.warning("not in memcache")
            q = Receit.query(ancestor = contact.key)
            receits = [ x for x in q ]
            memcache.set("receits_%s" % contact.key.urlsafe(), receits)
            if car:
                q = q.filter(Receit.car == car.key)
            if service:
                q = q.filter(Receit.service == service.key)
        if limit and len(receits) > limit:
            return receits[:limit]
        return receits
    
    @classmethod
    def mem(cls,contact):
        receits = memcache.get("receits_%s" % contact.key.urlsafe())
        return receits
    
        