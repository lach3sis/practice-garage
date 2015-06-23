from practice.handlers import BasicHandler
from practice.model.car import Car
from practice.model.garage import Garage
from google.appengine.ext import blobstore
from google.appengine.api import images
from google.appengine.ext import ndb
from google.appengine.ext.webapp import blobstore_handlers
from practice.model.car_avatar import CarAvatar


class  CarAvatarHandler(blobstore_handlers.BlobstoreUploadHandler):
    
    def put(self):
            import logging
            car_key = self.request.get('car')
            car = car_key.get()
            
            if not (car):
                
                logging.error("No car available")
            else:
                logging.warn("Found car: %s" % car)
            
            avatar = self.request.get('img')
#             avatar = images.resize(avatar, 50, 50,)
            car.avatar = avatar
                
            car.put()
            logging.warn("image save is a succes!")
            
                       
    def post(self):
        import logging
        try:
            upload = self.get_uploads()[0]
            carkey_ident = self.request.get('car')
            print "from request %s" % carkey_ident
            car = Car.get(carkey_ident)
            
            if car:
                cark = ndb.Key('Car', car.key.id())
                car_avatar = CarAvatar(car_key=cark, blob_key=upload.key())
                avatar = car_avatar.save()
                logging.warn(avatar.blob_key)
                car.avatar = avatar.blob_key
#                 self.redirect('/view_photo/%s' % upload.key())
                car.save()
                
                              
                
        except:
            logging.error('error image cannot be saved')
            
            
class ViewPhotoHandler(blobstore_handlers.BlobstoreDownloadHandler):
    def get(self, photo_key):
        if not blobstore.get(photo_key):
            self.error(404)
        else:
#             self.response.out.write("<div><img src='img?img_id=%s'></img>" % photo_key())
            self.send_blob(photo_key)           