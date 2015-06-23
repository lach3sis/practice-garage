from practice.handlers import BasicHandler
from practice.model.car import  Car
# from aetypes import Boolean
from google.appengine.ext import ndb
import logging


class ContactHandler(BasicHandler):
    """ Handler for Contact
    
        Supports up to 3 parameters
        key = always a garage id
        topic = what you want to do
        ident = Can be id of another class as child from Contact
    """
    
    def get(self, car="", key="",topic=""):
        
        
        if key:
            contactkey =  ndb.Key('Contact', key)
            contact = contactkey.get()
            self.render_response("/detail/contact-list.html", contact=contact)
            
        elif car and not key:

            carkey = ndb.Key('Car', int(car))
            c = carkey.get()
            contacts =  c.listcontact()
            self.render_response("/detail/contact-list.html", contacts=contacts)

#         elif not car and key:
#             contacts = Car.get(key)
#             self.render_response("/detail/car-list.html", cars=cars)
#         else:
# 
#             car = Car.get(key)
# 
#             if topic == "":
#                 
#                 self.render_response("/detail/car-edit.html", car=car)


    def put(self, ident, car_ident):
        ''' get the contact you want to edit
            then save your edited contact
        '''
        
        if car_ident:
            carkey = ndb.Key('Car', car_ident)
            car = carkey.get()
            contact = car.listcontact()
        elif(ident and not car_ident):
            contactkey = ndb.Key('Contact', ident)
            contact = contactkey.get()
            
        if contact:
            props = {"name": self.request.get('name'), "email": self.request.get('email'),
                     "tel_nr": self.request.get('tel_nr'), "klootfactor": self.request.get('klootfactor'),
                     "car": self.request('car'), "gender": self.request.get('gender')}
            contact.update(ident, props)


    def delete(self, ident="", topic=""):
        car = Car.get(ident)
        Car.delete(car)
        
        
    def post(self, ident="", topic=""):
        
        props = {
                 'name': self.request.get('name'),
                 'email' : self.request.get('email'),
                 'tel_nr' : self.request.get('tel_nr'),
                 'klootfactor': self.request.get('klootfactor'),
                 'car': self.request.get('car'),
                 'gender': self.request.get('gender')
                 }
        car = Car.get(self.request.get('car'))
        if(len(car.listcontact()) == 0):
            car.add_carcontact(props)
            

        elif(len(car.listcontact()) > 0):
            contactlist = car.listcontact()
            contact = contactlist[0]
            check = contact.update(contact.key.id(), props)
            logging.warn(check)         