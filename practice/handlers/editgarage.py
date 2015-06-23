from practice.handlers import BasicHandler
from practice.model.garage import Garage


class EditGarageHandler(BasicHandler):
    """ Handler for Testpage
    
        Supports up to 3 parameters
        key = always a garage id
        topic = what you want to do
        ident = Can be id of another class as child from Garage
    """
    
    def get(self, garagekey):
        
        garage = Garage.get(garagekey)
        import logging
        logging.warn(garage)
        self.render_response("garage_profile.html", garage=garage)
