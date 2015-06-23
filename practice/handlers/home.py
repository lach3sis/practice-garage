from practice.handlers import BasicHandler
from practice.model.garage import Garage


class HomePage(BasicHandler):
    """ Handler for Garage
    
        Supports up to 3 parameters
        key = always a garage id
        topic = what you want to do
        ident = Can be id of another class as child from Garage
    """
    
    def get(self):
        
        garages = Garage.query()
        
        self.render_response("/home.html", garages=garages)

    def post(self, ident="", topic=""):
            props = {'name': self.request.get('name'),
                     'brand': self.request.get('brand'),
                     'note': self.request.get('note'),
                     'country': self.request.get('country'),
                      'price_per_hours': self.request.get('price_per_hours'),
                      'round_op_hours': self.request.get('round_up_hours')}
            Garage.add(props)