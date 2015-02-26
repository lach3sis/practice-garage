from google.appengine.ext import ndb


class Garage(ndb.Model):
    
    name = ndb.StringProperty(required=True)
    brand = ndb.StringProperty()
    
    note = ndb.TextProperty(indexed=False)
    price_per_hours = ndb.FloatProperty()
    roundup_workhrs = ndb.BooleanProperty()

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
    
    
    @classmethod
    def add(cls, params):
        c = Garage()
        c.fill(params)
        c.put()
        return c
    
    def fill(self, params):
        if 'name' in params:
            self.name = params.get('name')
        if 'brand' in params:
            self.brand = params.get('brand')
        if 'note' in params:
            self.note = params.get('note')
        if 'price_per_hours' in params:
            self.price_per_hours = params.get('price_per_hours')
        if 'roundup_workhrs' in params:
            self.roundup_workhrs = params.get('roundup_workhrs')
    
    def save(self):
        self.put()
