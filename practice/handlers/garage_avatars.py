

from practice.model.garage import Garage
from google.appengine.ext import blobstore
#from google.appengine.api import images
from google.appengine.ext import ndb
from google.appengine.ext.webapp import blobstore_handlers
from practice.model.garage_avatar import GarageAvatar


class  GarageAvatarHandler(blobstore_handlers.BlobstoreUploadHandler):
    
    def put(self):
            import logging
            garage_key = self.request.get('garage')
            garage = garage_key.get()
            
            if not (garage):
                
                logging.error("No garages available")
            else:
                logging.warn("Found garage: %s" % garage)
            
            avatar = self.request.get('img')
#             avatar = images.resize(avatar, 50, 50,)
            garage.avatar = avatar
                
            garage.put()
            logging.warn("image save is a succes!")
            
                       
    def post(self):
        import logging
        
        try:
            upload = self.get_uploads()[0]
            garagekey_ident = self.request.get('garage')
            print "from request %s" % garagekey_ident

            garage = Garage.get(garagekey_ident)
            
            if garage:
                key = ndb.Key('Garage', (int(garagekey_ident)))
                garage_avatar = GarageAvatar(garage_key=key, blob_key=upload.key())
                avatar = garage_avatar.save()
                logging.warn(avatar.blob_key)
                garage.avatar = avatar.blob_key
#                 self.redirect('/view_photo/%s' % upload.key())
                garage.save()
    
        except:
            logging.error('error image cannot be saved')
            
            
class ViewGaragePhotoHandler(blobstore_handlers.BlobstoreDownloadHandler):
    def get(self, photo_key):
        if not blobstore.get(photo_key):
            self.error(404)
        else:
#             self.response.out.write("<div><img src='img?img_id=%s'></img>" % photo_key())
            self.send_blob(photo_key)           