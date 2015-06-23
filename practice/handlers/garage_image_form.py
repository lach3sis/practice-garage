from practice.handlers import BasicHandler
from google.appengine.ext import blobstore


class GarageImageForm(BasicHandler):
    
    
    def get(self, ident=None):
        
        upload_url = blobstore.create_upload_url('/upload_garage_avatar')
#         key = ndb.Key("Car", int(ident))
        
#         self.render_response("/detail/add_image.html", car=car)
        self.response.out.write('<form action="%s" method="POST" enctype="multipart/form-data">' % upload_url)
        self.response.out.write('''Upload File:  <input type="hidden" id="garage" name="garage" value="%s">
        <input type="file" name="file"><br> <input type="submit"
            name="submit" value="Submit"> </form></body></html>''' % ident)