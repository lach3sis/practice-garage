
from google.appengine.ext import ndb


class Garage(ndb.Model):
    
    name = ndb.StringProperty(required=True)
    brand = ndb.StringProperty()
    
    note = ndb.TextProperty(indexed=False)
    
    @classmethod
    def get(cls, key):
        return ndb.Key("Garage", int(key)).get()
    
    @classmethod
    def list(cls, name=None, brand=None, limit=20):
        q = Garage.query()
        if name:
            q.filter(Garage.name, name)
        elif brand:
            q.filter(Garage.brand, brand)
        if limit:
            return q.fetch(limit)
        return q

    def fill(self, params):
        if 'name' in params:
            self.name = params.get('name')
        if 'brand' in params:
            self.brand = params.get('brand')
        if 'note' in params:
            self.note = params.get('note')
    
    def save(self):
        import logging
        logging.warning("putting it in datastore :O")
        self.put()
