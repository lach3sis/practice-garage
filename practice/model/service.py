import logging
from google.appengine.ext import ndb
from google.appengine.api import memcache


class Service(ndb.Model):
    replacement_part = ndb.StringProperty(required=False)
    price_part = ndb.FloatProperty(required=False)
    worked_hrs = ndb.FloatProperty(required=True)
    

    def fill(self,c):
        if 'replacement_part' in c:
            self.replacement_part = c['replacement_part']
        if 'price_part' in c:
            self.price_part = c['price_part']
        if 'worked_hrs' in c:
            self.worked_hrs = c['worked_hrs']
            
    def save(self):
        self.put()
        memcache.delete(self.key.parent().urlsafe())
        
    def update(self, props):
        from practice.model.car import Car
        self.fill(props)
        self.save()
        car = self.key.parent().get()
#         Car.calculate1(car, self.list(car))
        car.calculate()
     
    def delete(self):
        self.key.delete()
        # parent key ophalen.
        memcache.delete("services_%s" % self.key.parent().urlsafe())
        self.key.parent().get().calculate()
    
    @staticmethod
    def multiadd(car,servicelist):
#         car = self.key.parent().get()
        print "ADDING %s Services" % len(servicelist)
        p = ndb.put_multi(servicelist)
        memcache.delete("services_%s" % car.key.urlsafe())
        car.calculate1(servicelist)
        return p
    
#     @classmethod
#     def add(cls, car, c):
# 
#         s = Service(parent=car.key)
#         s.fill(c)
#         s.save()
#         car.calculate(self)
#         return s

    @classmethod
    def add(cls, car, c):

        s = Service(parent=car.key)
        s.fill(c)
        s.save()
        memcache.delete("services_%s" % car.key.urlsafe())
        car.calculate()
        return s
        
    @staticmethod
    def get(ident, carkey):
        key = ndb.Key("Service", int(ident), parent=carkey)
        service = key.get()
        return service
     
    @classmethod
    def list(cls, car, replacement_part=None, limit = 20):
        services = memcache.get(car.key.urlsafe())
        if not services:
            q = Service.query(ancestor=car.key)
            services = [ x for x in q ]
            memcache.set("services_%s" % car.key.urlsafe(), services)
            if replacement_part:
                logging.warn("Searching for %s" % replacement_part)
                q = q.filter(Service.replacement_part == replacement_part)
        if limit and len(services) > limit:
            return services[:limit]
        return services
