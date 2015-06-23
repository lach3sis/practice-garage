from practice.handlers import BasicHandler
from practice.model.garage import Garage
# from aetypes import Boolean


class Garages2(BasicHandler):
    """ Handler for Garage
    
        Supports up to 3 parameters
        key = always a garage id
        topic = what you want to do
        ident = Can be id of another class as child from Garage
    """
    
    def get(self, key="", topic="", ident=""):
        if not key or key == "":
            garages = Garage.query()
            self.render_response("/detail/garage_list_new.html", garages=garages)
        else:
            import logging
                    
            garage = Garage.get(key)
#             logging.warning(garage.name)
            if topic == "":
                
#                 logging.warning("garage.name")
                self.render_response("/detail/garage-edit.html", garage=garage)

    def put(self, params):
        
        #get the garage you want to edit
        import logging
        logging.error(params)
        currentgarage = Garage.get(params)
        logging.error("before : %s" % currentgarage)
        #fill it up with new values
        currentgarage.name = self.request.get('name')
        currentgarage.brand = self.request.get('brand')
        currentgarage.note = self.request.get('note')
        logging.error("after: %s" % currentgarage)
        currentgarage.postal_country = self.request.get('postal_country')
        currentgarage.price_per_hour = float(self.request.get("price_per_hour"))
        currentgarage.roundup_workhrs = bool(self.request.get('round_up_workhrs'))
        #now save your edited garage
        currentgarage.save()
#         import  logging
#         logging.warning(params.name)
#         currentgarage = Garage.get(params.key)
#         
#         logging.warn("huidige garage %s" % currentgarage)


    def delete(self, ident="", topic=""):
        import logging
        logging.warning(ident)
        currentgarage = Garage.get(ident)
        logging.warning(currentgarage)
        Garage.delete(currentgarage)
        
    def post(self, ident="", topic=""):
        props = {'name': self.request.get('name'),
                 'brand': self.request.get('brand'),
                 'note': self.request.get('note'),
                 'country': self.request.get('country'),
                  'price_per_hours': self.request.get('price_per_hours'),
                  'round_op_hours': self.request.get('round_up_hours')}
        Garage.add(props)