from google.appengine.ext import ndb


class CarAvatar(ndb.Model):
    car_key = ndb.KeyProperty()
    blob_key = ndb.BlobKeyProperty()
    
    def fill(self, param):
        '''Fill Contact entity with properties
        '''
        print param
        if 'name' in param:
            self.name = param['name']
        if 'email' in param:
            self.email = param['email']
            
    def save(self):
        self.put()
        return self
    
#     @classmethod
#     def add(cls, car, g):
#         '''Add a new contact
#         '''
#         carkey = ndb.Key('Car', car)
#         c = Contact(parent = carkey)
#         c.fill(g)
#         c.put()
#         memcache.delete("contacts_%s" %carkey.urlsafe())
#         return c


    @classmethod
    def list(cls, blob_key=None, car_key=None):
        pass
    
    
    