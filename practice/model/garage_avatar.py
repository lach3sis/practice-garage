from google.appengine.ext import ndb


class GarageAvatar(ndb.Model):
    garage_key = ndb.KeyProperty()
    blob_key = ndb.BlobKeyProperty()
    
    def fill(self, param):
        '''Fill Contact entity with properties
        '''
        print param
        if 'garage_key' in param:
            self.garage_key = param['garage_key']
        if 'blob_key' in param:
            self.blob_key = param['blob_key']
            
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
    
    
    