import webapp2
from src.handlers.garages import Garages
# from google.appengine.ext.webapp.util import run_wsgi_app


class MainPage(webapp2.RequestHandler):
    
    
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('Hello, webapp World!')


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/home', Garages),
    
    ('/garage', Garages),
    ('/garage/(.*)', Garages)
    ], debug=True)

# 
# def main():
#     run_wsgi_app(application)
# 
# if __name__ == "__main__":
#     main()
