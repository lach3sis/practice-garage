from practice.handlers import BasicHandler
from practice.model.car import Car
from practice.model.garage import Garage

class  CarprofHandler(BasicHandler):
    
    def get(self, ident):
            
            car = Car.get(ident)
            garage = Garage.get(car.garage.id())
            import logging
            logging.warn(car)
            self.render_response("/detail/car_temp_profile.html", car=car, garage=garage)