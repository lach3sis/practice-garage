from google.appengine.ext import ndb
import logging
 
class Car(ndb.Model):
    garage = ndb.KeyProperty(required=True)
    brand = ndb.StringProperty(required=True)
    name = ndb.StringProperty(required=True)
    garage_name = ndb.StringProperty(required=False)
     
    def fill(self,c):
        
        self.garage = c['garage']
        self.brand = c['brand']
        self.name = c['name']
        self.garage_name = c['garage_name']
     
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
     
    @staticmethod
    def list(garage=None):
        q = Car.query()
        if garage:
            q = q.filter(Car.garage == garage.key)
        logging.warning(Car.query().count())
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