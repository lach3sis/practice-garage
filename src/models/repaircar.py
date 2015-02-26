import logging

from google.appengine.ext import ndb


class Service(ndb.Model):
    replacement_part = ndb.StringProperty(required=False)
    price_part = ndb.FloatProperty(required=False)
    worked_hrs = ndb.FloatProperty(required=True)
    
     
    def fill(self,c):
        logging.warning(c)
        #edit
        if 'replacement_part' in c:
            self.replacement_part = c['replacement_part']
        if 'price_part' in c:
            logging.warning("got a price part")
            self.price_part = c['price_part']
        self.worked_hrs = c['worked_hrs']
        
     
    def save(self):
        self.put()
     
    def delete(self):
        logging.warning("delete function in repairCar.py")
        self.key.delete()
     
    @classmethod
    def add(cls, car, c):
        s = Service(parent=car.key)
        s.fill(c)
        s.put()
        return s
        
    @staticmethod
    def get(ident, carkey):
        key = ndb.Key("Service", int(ident), parent=carkey)
        service = key.get()
        logging.warning("Current ID number : %s" % ident)     
        logging.warning("Current key is : %s" % key)
        
        return service
     
    @classmethod
    def list(cls, car, limit = 20):
        q = Service.query(ancestor=car.key)
        if limit:
            return q.fetch(limit)
        return q
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