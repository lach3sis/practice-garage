from practice.handlers import BasicHandler
from practice.model.car import  Car
from practice.model.garage import Garage
# from aetypes import Boolean
from google.appengine.ext import ndb
from google.appengine.api import memcache

class CarHandler(BasicHandler):
    """ Handler for Garage
    
        Supports up to 3 parameters
        key = always a garage id
        topic = what you want to do
        ident = Can be id of another class as child from Garage
    """
    
    def get(self, garage="", key="",topic=""):
        
            
        if garage:
            garagekey = ndb.Key('Garage', garage)
            cars =  Car.listtest(garagekey)

            self.render_response("/detail/car-list.html", cars=cars)

        elif not garage and key:
            cars = Car.get(key)
            self.render_response("/detail/car-list.html", cars=cars)
        else:

            car = Car.get(key)

            if topic == "":
                
                self.render_response("/detail/car-edit.html", car=car)


    def put(self, ident):
        ''' get the garage you want to edit
            then save your edited garage
        '''
        props = {"name": self.request.get('name'), "brand": self.request.get('brand')}
        Car.update(self.request.get('id'), props)
        print ("After : %s" % props)


    def delete(self, ident="", topic=""):
        car = Car.get(ident)
        Car.delete(car)
        
        
    def post(self, ident="", topic=""):
        props = {
                 'name': self.request.get('name'),
                 'brand': self.request.get('brand'),
                 'garage': self.request.get('garage')
                 }
        
        Car.add(props)
