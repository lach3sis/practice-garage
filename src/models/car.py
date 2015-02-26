import logging

from google.appengine.ext import ndb
from src.models.garage import Garage
from src.models.repaircar import Service


class Car(ndb.Model):
    garage = ndb.KeyProperty(required=True)
    brand = ndb.StringProperty(required=True)
    name = ndb.StringProperty(required=True)
    
#     k1 = ndb.KeyProperty(required = False)
     
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
        logging.warning("Current ID number : %s" % ident)
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
    
#     def calculate(self, worked_hrs=0.0, price_per_hours=0.0, price_part=0.0):    
#         if price_part:
#             totaal = (worked_hrs * price_per_hours) + price_part
#         else:
#             totaal = price_per_hours * worked_hrs
#             return totaal
#         return totaal
#     
    def calculate2(self):
        def calc(self, worked_hrs=0.0, price_per_hours=0.0, price_part=0.0):
            if price_part:
                totaal = (worked_hrs * price_per_hours) + price_part
            else:
                totaal = price_per_hours * worked_hrs
                return totaal
            return totaal  
        for p in Service.list(self):
            if p.price_part:
                return calc(self, p.worked_hrs, self.garage.get().price_per_hours, p.price_part)
            else:
                return calc(self, p.worked_hrs, self.garage.get().price_per_hours)           
     
    def calculate3(self):
        total = 0.0
        def calc(self, worked_hrs=0.0, price_per_hours=0.0, price_part=0.0):
            if price_part:
                return (worked_hrs * price_per_hours) + price_part
            else:
                return (price_per_hours * worked_hrs) 
        for p in Service.list(self):
            total = total + calc(self, p.worked_hrs, self.garage.get().price_per_hours, p.price_part)
        return total
            
    
    @staticmethod
    def list(garage=None, limit=20):
        q = Car.query()
        if garage:
            q = q.filter(Car.garage == garage.key)
        if limit:
            return q.fetch(limit)
        return q.order(Car.name)
        
#         to_delete = []
#         for a in Car.query():
#             if a.garage.get():
#                 logging.warning(a.name + " belongs to " + a.garage.get().name)
#             else:
#                 to_delete.append(a.key)
#         logging.warning('delete number: ' + str(len(to_delete)))
#         ndb.delete_multi(to_delete)
#         test = q.fetch(100)
#         logging.warning(len(test))
#         return test