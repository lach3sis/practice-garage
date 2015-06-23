from practice.handlers import BasicHandler
from practice.model.car import  Car
from practice.model.service import Service
from practice.model.receit import Receit
import logging
# from aetypes import Boolean
from google.appengine.ext import ndb


class addServiceHandler(BasicHandler):
    """ Handler for Services
    
    """
    def get(self, carkey, ident="", topic=""):
        
        if topic and topic== "get_servicecosts" and ident is not None:
            service = Service.get(ident, carkey)
            
            car = service.key.parent().get()
            contactlist = car.listcontact()
            contact = contactlist[0]
            price_per_hours = car.garage.get().price_per_hours
            klootfactor = contact.klootfactor
            worked_hrs = service.worked_hrs
            price_part = service.price_part
            
            costs = car.calc_single_service(price_part, worked_hrs, price_per_hours, klootfactor)
            
            return costs
            

        elif ident:
            car = Car.get(carkey)
            logging.warn(car)
            self.render_response("/detail/add_service.html", car=car)
        else:  
            car = Car.get(int(carkey))
            logging.warn(car)
            self.render_response("/detail/add_service.html", car=car)

    def put(self, ident, carkey):
        ''' get the garage you want to edit
            then save your edited garage
        '''
        props = {"replacement_part": self.request.get('replacement_part'), "price_part": self.request.get('price_part'), "worked_hrs": self.request.get('worked_hrs')}         
        service = Service.get(ident, carkey)
        service.update(props)

    def delete(self, ident, carkey):
        '''deletes a service
        '''        
        service = Service.get(ident, carkey)
        service.delete()


    def post(self, params):
        ''' adds a new service
            needs a car instance and dict with string replacement_part, float worked_hrs, float price_part
        '''

        
        carid = self.request.get('carid')
        car = Car.get(carid)
                
        Service.add(car, {"replacement_part": self.request.get("replacement_part"), 
                         "price_part": float(self.request.get('price_part')), "worked_hrs": float(self.request.get('worked_hrs'))})
        
        
        self.response.out.write(carid)
        
        
class ServiceHandler(BasicHandler):
    """ Handler for Services
    
    """
    
    def get(self, carkey, ident="", topic=""):
        
        
        
        if self.request.get('topic') :
            ident = self.request.get('ident')

            carkey = self.request.get('carkey')
            cark = ndb.Key('Car', int(carkey))

            service = Service.get(ident,cark)

            car = service.key.parent().get()
            from practice.model.garage import Garage
            garage = Garage.get(car.garage.id())
            contactlist = car.listcontact()
            contact = contactlist[0]


            klootfactor = contact.klootfactor
            worked_hrs = service.worked_hrs
            price_part = service.price_part
            
            costs = car.calc_single_service(price_part, worked_hrs, garage.price_per_hours, klootfactor)
            
            print car.calculate()
            
            self.response.out.write( costs )
        
        elif ident and topic != None:
            car = Car.get(carkey)
            print car.listservices()
            logging.warn(car)
            self.render_response("/detail/service-list.html", car=car)
        else:  
            car = Car.get(int(carkey))
            services = car.listservices()
            receit = car.calculate()
            logging.warn(car)
            self.render_response("/detail/service-list.html", receit=receit, services=services)

    def put(self, ident, carkey):
        ''' get the garage you want to edit
            then save your edited garage
        '''
        props = {"replacement_part": self.request.get('replacement_part'), "price_part": self.request.get('price_part'), "worked_hrs": self.request.get('worked_hrs')}         
        service = Service.get(ident, carkey)
        service.update(props)

    def delete(self, ident, carkey):
        '''deletes a service
        '''        
        service = Service.get(ident, carkey)
        service.delete()


    def post(self, params):
        ''' adds a new service
            needs a car instance and dict with string replacement_part, float worked_hrs, float price_part
        '''

        
        carid = self.request.get('carid')
        car = Car.get(carid)
        
       
#         shit = {"replacement_part": self.request.get("replacement_part"), 
#                           "price_part": self.request.get('price_part'), "worked_hrs": self.request.get('worked_hrs')}
        
        
   
            
        Service.add(car, {"replacement_part": self.request.get("replacement_part"), 
                         "price_part": float(self.request.get('price_part')), "worked_hrs": float(self.request.get('worked_hrs'))}
                              )
        
        
        self.response.out.write(carid)
        
        
        