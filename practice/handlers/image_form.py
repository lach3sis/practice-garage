from practice.handlers import BasicHandler

from google.appengine.ext import ndb
from google.appengine.ext import blobstore


class imageForm(BasicHandler):
    
    
    def get(self, ident=None):
        
        
        upload_url = blobstore.create_upload_url('/upload_avatar')
#         key = ndb.Key("Car", int(ident))
        
#         self.render_response("/detail/add_image.html", car=car)
        self.response.out.write( '<form action="%s" method="POST" enctype="multipart/form-data">' % upload_url )
        self.response.out.write( '''Upload File:  <input type="hidden" id="car" name="car" value="%s">
        <input type="file" name="file"><br> <input type="submit"
            name="submit" value="Submit"> </form></body></html>''' % ident )
    
        
class imageModalForm(BasicHandler):
    
    
    def get(self, ident=None):
        
        upload_url = blobstore.create_upload_url('/upload_avatar')
        self.response.out.write( ''''<div class="modal-dialog">
                                    <div class="modal-content">
                                    <div class="modal-header">
                                    <h2>Model 1</h2>
                                    </div>
                                    <div class="modal-body">''' )
        self.response.out.write( '<form action="%s" method="POST" enctype="multipart/form-data">' % upload_url )
        self.response.out.write( '''Upload File:  <input type="hidden" id="car" name="car" value="%s">
                                    <input type="file" name="file"> <br> 
                                    <input type="submit" name="submit" value="Submit"> 
                                    </form>
                                    </div>
                                    <div class="modal-footer">
                                    <button type="button" class="btn btn-primary" data-dissmiss="modal"> Close</button>
                                    </div>
                                    </div>
                                    </div>''' % ident ) 