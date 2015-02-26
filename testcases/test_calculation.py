""" Very simple example how to use the BasicTestCase
"""

from src.models.car import Car
from src.models.contact import Contact
from src.models.garage import Garage
from src.models.repaircar import Service
from testcases import BasicTestCase


class GarageTestCase(BasicTestCase):
    
    def setUP(self):
        ''' This method can be used to import or set up some data needed for every testcase
            
            no need to call super
        '''
        pass
    
    def ptest_this(self):
        
        # Garage1
        g = Garage()
        g.name ="Garage GeldWolven"
        g.brand = "BMW"
        g.note = "Get Ripped of"
        g.price_per_hours = 10.00
        g.roundup_workhrs = False
        
        g.put()
        
        # Define a new Car
        car_params = {"name": "200304 NX",
                      "brand": "Nissan"}
        # Store Car to datastore
        c = Car.add(g, car_params)
        
        # Define a new Car
        car2_params = { 'name': '45354 GAS',
                        'brand': 'Nissan'}
        # Store Car to datastore
        Car.add(g, car2_params)

        # Define a Service
        s1_params = {"replacement_part": "Exhaust",
                    "price_part": 155.08,
                    "worked_hrs": 8}
        #Store Service to Datastore
        Service.add(c, s1_params)
        
        #Define a Service
        s2_params = {"worked_hrs": 15.55}
        #Store Service to Datastore
        Service.add(c, s2_params)
        
        #Define a Service
        s3_params = {"replacement_part": "Radio",
                    "price_part": 28,
                    "worked_hrs":1.25}
        #Store Service to Datastore
        Service.add(c, s3_params)
        
        #Define a new Contact
        contact1_params = {"name": "Tim Tukkie",
                           "email": "example@mail.nl",
                           "tel": "0315-3332225"}
        #Store Contact to Datastor
        Contact.add(g, contact1_params)
        
        # Define a new Contact
        contact2_params = {"name": "Tim Burton",
                   "email": "example123@mail.nl",
                   "tel": "0315-3332335"}
        # Store Contact to Datastore
        Contact.add(g, contact2_params)
    
    def test_dt(self):
        
        g = Garage()
        g.name="Bugatti Inc."
        g.brand="Bugati"
        g.note="All is sold at double the price!"
        g.price_per_hours = 45
        g.roundup_workhrs = True
        
        c = Car()
        c.name = "776GZ"
        c.brand ='Toyota'
        c.garage = g.key
        c.garage_name = g.name
        
        c2 = Car()
        c2.name = '3003GZ'
        c2.brand = 'Toyota'
        c2.garage = g.key
        c2.garage_name = g.name
        
        g1= Garage()
        g1.name ="DonEnCor"
        g1.brand = "Nissan"
        g1.note = "testnote"
        g1.price_per_hours = 78.54
        g1.roundup_workhrs = False

        s = Service()
        s.car = c.key
        s.replacement_part = '4 wheels'
        s.price_part = 76.86
        s.worked_hrs = 2.2
        
        g.put()
        c.put
        g1.put()
        s.put()
        
    
    def kljtest_new(self):
        
        garage1 = Garage(name='dummie garage',
                         brand='Toyota',
                         note='Closed',
                         price_per_hours=56,
                         roundup_workhrs=True)
        garage1.put()
        
        garage2 = Garage ( name = 'ZupaDupa',
                           brand = 'Porsche',
                           note = 'Open',
                           price_per_hours = 44.3,
                           roundup_workhrs = False)
        garage2.put()
        
        
        car1 = Car( name = 'Fastcar101',
                    brand= 'Toyota',
                    garage = garage1.key )
        car1.put()
        
        car2 = Car(name = 'RX493',
                   brand = 'Suzuki',
                   garage = garage1.key)
        c2key = car2.put()
        
        car3 = Car( name = 'RL4402',
                    brand = 'Fiat',
                    garage = garage2.key)
        c3key = car3.put(
                         )
        serv1 = Service(replacement_part = 'Chair',
                        price_part = 4.53,
                        worked_hrs = 4.0,
                        parent = car2.key
                        )
        serv1.put()
        
        serv2 = Service (replacement_part = 'Roof',
                         price_part = 7897.95,
                         worked_hrs = 21,
                         parent = car2.key)
        serv2.put()
        
        serv3 = Service( worked_hrs = 45,
                         parent = car1.key
                         )
        serv3.put()
        
        serv4 = { "replacement_part" : 'Clotch',
                  "price_part" : 878,
                  "worked_hrs" : 12
                 }
        
        Service.add(car1, serv4)
        
        contact1 = Contact( name = 'Piet Jan',
                            email = 'sample@example.nl',
                            tel_nr = '0314324886',
                            parent = c2key)
        contact1.put()
        
        contact2 = Contact( name = 'Floris',
                            email = 'Sample@upc.nl',
                            tel_nr = '0254445987',
                            parent = c3key)
        contact2.put()
        
        
    def create_garage(self, data):
        return Garage.add(data)
    
    def create_car(self, garage, data):
        return Car.add(garage, data)
    
    def create_service(self, car, data):
        Service.add(car, data)
    
    def create_contact(self, car, data):
        Contact.add(car, data)
        
    def calczzzzz(self, garage, car, data, result):
        self.create_service(car, data)
        self.assertEqual(result, car.calculate3())
        
        
    def test_01(self):

        #New Garage #1
        g = self.create_garage({"name": "GarageDubi", "brand": "Porsche", "price_per_hours": 12})

        #New Car #1.1
        
        c = self.create_car(g, {"name": "FastName", "brand": "Nissan"})

        #New Contact #1.1.1

        #New Service #1.1.1
        data = {"replacement_part": 'Windows', "price_part": 18, "worked_hrs":12}
        #New Service #1.1.2
#         self.create_service(c, {"replacement_part": 'Ashtray', "price_part": 200, "worked_hrs":7.9})
        print "Garage 1 auto 1"
        #Calculate Costs
#         self.assertEqual(456.8, c.calculate3())
        self.calczzzzz(g, c, data, 456.8)

        #New Car #1.2
        c = self.create_car(g, {" name": "SlowName", "brand": "Mazda"})
        #New Contract #1.2.1
        self.create_contact(c, {"name": "peter", "email" : "sample@sample.nl"})
        #New Service #1.2.1
        self.create_service(c, {"replacement_part": "YourGrandma", "price_part": 1566, "worked_hrs":156})
        #New Service #1.2.2
        self.create_service(c, {"replacement_part": "Oil", "price_part":548, "worked_hrs":12})
        #New Service #1.2.3
        self.create_service(c, {"worked_hrs": 1213})
        print "Garage 1 auto 2"        
        #Calculate Costs
        self.assertEqual(18686, Car.calculate3(c))
        
        #New Garage #2
        g = self.create_garage({"name": "GarageFlut", "brand": "Nissan", "price_per_hours": 15})
        #New Car #2.1
        c = self.create_car(g, {"name": 'BlingBling2000', "brand" : "Suzuki"})
        #New Contact #2.1.1         
        self.create_contact(c, {"name": "Mark", "email": "testing@test.nl", "tel_nr": "070-22332225"})
        #New Service #2.1.1
        self.create_service(c, {"replacement_part": "Brakes", "price_part": 122, "worked_hrs":34})
        #New Service #2.1.2
        self.create_service(c, {"replacement_part": "Chip-Tune_RD664570", "price_part": 215, "worked_hrs":17.2})
        print "Garage 2 auto 1"        
        #Calculate costs
        self.assertEqual(1105, Car.calculate3(c))
        
        #New Garage 3
        g = self.create_garage({"name": "HydroTune", "brand": "Ford", "price_per_hours": 7.5})
        #New Car 3.1
        c = self.create_car(g, {"name": 'ZingZagius', "brand" : "ZZ-Tupi"})
        #New Contact 3.1.1
        self.create_contact(c, {"name": "Kevin", "email": "kevin@test.nl", "tel_nr": "070-454654878"})
        #New Service 3.1.1
        self.create_service(c, {"replacement_part": "Brakes", "price_part": 46, "worked_hrs": 8})
        #New Service 3.1.2
        self.create_service(c, {"replacement_part": "Clutch", "price_part": 400, "worked_hrs": 18})
        print "Garage 3 auto 1"        
        #Calculate costs
        self.assertEqual(641, Car.calculate3(c))
        
        g = None
        c = None
        
    def tearDown(self):
        """ tearDown will be called after a testcase
        """
        pass