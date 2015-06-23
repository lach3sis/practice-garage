from practice.handlers import BasicHandler



class Testpage(BasicHandler):
    """ Handler for Testpage
    
        Supports up to 3 parameters
        key = always a garage id
        topic = what you want to do
        ident = Can be id of another class as child from Garage
    """
    
    def get(self):
        
        self.render_response("test1.html")
