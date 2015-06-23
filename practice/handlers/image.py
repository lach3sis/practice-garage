from practice.handlers import BasicHandler
from google.appengine.ext import ndb

class Image(BasicHandler):
    def get(self):
        car_key = ndb.Key(urlsafe=self.request.get('car_id'))
        car = car_key.get()
        if car.avatar:
            self.response.headers['Content-Type'] = 'image/png'
            self.response.out.write(car.avatar)
        else:
            self.response.out.write('No image')
    