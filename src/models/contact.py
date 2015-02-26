from google.appengine.ext import ndb


class Contact(ndb.Model):
    name = ndb.StringProperty(required = True)
    email = ndb.StringProperty(required = True)
    tel_nr = ndb.StringProperty(required = False)
    
    
    def fill(self, param):
        if 'name' in param:
            self.name = param['name']
        if 'email' in param:
            self.email = param['email']
        if 'tel_nr' in param:
            self.tel_nr = param['tel_nr']
            
        
    def save(self):
        self.put()
        
        #Delete entity by key
    def delete(self):
        self.key.delete()
    
    @classmethod
    def add(cls, car, g):
        c = Contact(parent = car.key)
        c.fill(g)
        c.put()
        return c
    
    @staticmethod
    def get(ident, garagekey, limit=20):
        key = ndb.Key("Contact", int(ident), parent=garagekey)
        contact = key.get()
        return contact
    
    @classmethod
    def list(cls, garage):
        q = Contact.query(ancestor = garage.key)
        return q
    