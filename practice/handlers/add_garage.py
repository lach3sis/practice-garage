from practice.handlers import BasicHandler



class AddGarageHandler(BasicHandler):
    """ Form to add new garages.
    """
    
    def get(self):
        
        try:
            self.render_response("add_garageform.html")
        
        except:
            print "error getting garage form"