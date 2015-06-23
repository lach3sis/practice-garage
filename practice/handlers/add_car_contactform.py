from practice.handlers import BasicHandler
from practice.model.car import Car


class  CarContactForm(BasicHandler):
    """ Handler for Garage
        
            Supports up to 3 parameters
            key = always a garage id
            topic = what you want to do
            ident = Can be id of another class as child from Garage
        """
    
    def get(self, key="", topic="", ident=""):
        
        if not key or key == "":
            
            cars = Car.query()
            self.render_response("detail/frm_add_car_cntct.html", cars=cars)
            
        elif key:
            
            car = Car.get(key)
            self.render_response("detail/frm_add_car_cntct.html", car=car)
        
        else:
                    
            car = Car.get(key)
            
            if topic == "":

                self.render_response("/detail/car_temp_profile.html", car=car)

    