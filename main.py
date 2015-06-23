import webapp2
from practice.handlers.garages import Garages
from practice.handlers.home import HomePage
from practice.handlers.test1 import Testpage
from practice.handlers.editgarage import EditGarageHandler
from practice.handlers.showgarage import ShowGarageHandler
from practice.handlers.cars import CarHandler
from practice.handlers.carprofile import CarProfileHandler
from practice.handlers.showcar import CarprofHandler
from practice.handlers.car_avatars import CarAvatarHandler
from practice.handlers.garage_avatars import GarageAvatarHandler
from practice.handlers.car_avatars import ViewPhotoHandler
from practice.handlers.image_form import imageForm
from practice.handlers.image_form import imageModalForm
from practice.handlers.add_garage import AddGarageHandler
from practice.handlers.garage_image_form import GarageImageForm
from practice.handlers.garage_avatars import ViewGaragePhotoHandler
from practice.handlers.contacts import ContactHandler
from practice.handlers.services import addServiceHandler
from practice.handlers.services import ServiceHandler
from practice.handlers.get_garages import Garages2
from practice.handlers.add_car_contactform import CarContactForm


class MainPage(webapp2.RequestHandler):

    def get(self):
        
#         self.response.headers['Content-Type'] = 'text/plain'
#         self.response.out.write('Hello, webapp World!')

        self.redirect('/home')

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/home', HomePage),
    ('/test', Testpage),
    ('/add_garage', AddGarageHandler),
    ('/get_garages', Garages2),
    ('/garage', Garages),
    ('/garage/(.*)', Garages),
    ('/garage/(.*)/(.*)', Garages),
    ('/garages', Garages),
    ('/garages/(.*)', Garages),
    ('/editgarage/(.*)', EditGarageHandler),
    ('/showgarage/(.*)', ShowGarageHandler),
    ('/car', CarHandler),
    ('/cars', CarHandler),
    ('/car_profile/(.*)', CarProfileHandler),
    ('/car/(.*)', CarHandler),
    ('/contacts', ContactHandler),
    ('/load_add_carimg_modal/(.*)', imageModalForm),
    ('/contacts/(.*)', ContactHandler),
    ('/upload_avatar', CarAvatarHandler),
    ('/view_photo/([^/]+)?', ViewPhotoHandler),
    ('/upload_avatar/(.*)', imageForm),
    ('/view_garage_avatar/([^/]+)?', ViewGaragePhotoHandler),
    ('/upload_garage_avatar/(.*)', GarageImageForm),
    ('/upload_garage_avatar', GarageAvatarHandler),
    ('/car_img/(.*)', CarAvatarHandler),
    ('/add_service/(.*)', addServiceHandler),
    ('/services/(.*)', ServiceHandler),
    ('/addcontact_to_car/(.*)', CarContactForm),
    ('/carprofile/(.*)', CarprofHandler)
    ], debug=True)
