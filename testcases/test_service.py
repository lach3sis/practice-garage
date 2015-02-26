""" Very simple example how to use the BasicTestCase
"""

import logging
import math


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
        g.name = "Garage GeldWolven"
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
        c2 = Car.add(g, car2_params)
#         c = Car()
#         c.name = 
#         c.brand = "
#         c.garage = g.key
#         c.garage_name = g.name
#         logging.warning(c)
#         
#         c.put()

        # Define a Service
        s1_params = {"replacement_part": "Exhaust",
                    "price_part": 155.08,
                    "worked_hrs": 8}
        # Store Service to Datastore
        Service.add(c, s1_params)
        
        # Define a Service
        s2_params = {"worked_hrs": 15.55}
        # Store Service to Datastore
        Service.add(c, s2_params)
        
        # Define a Service
        s3_params = {"replacement_part": "Radio",
                    "price_part": 28,
                    "worked_hrs":1.25}
        # Store Service to Datastore
        Service.add(c, s3_params)
        
        # Define a new Contact
        contact1_params = {"name": "Tim Tukkie",
                           "email": "example@mail.nl",
                           "tel": "0315-3332225"}
        # Store Contact to Datastor
        Contact.add(g, contact1_params)
        
        # Define a new Contact
        contact2_params = {"name": "Tim Burton",
                   "email": "example123@mail.nl",
                   "tel": "0315-3332335"}
        # Store Contact to Datastore
        Contact.add(g, contact2_params)
        
#         s = Service()
#         s.replacement_part = 'Exhaust'
#         s.price_part = 235.56
#         s.worked_hrs = 8
#         
#         s.add(self, c.key, s)
        
        # Define a new Service
        s4_params = {"replacement_part": "Steering wheel",
                     "price_part": 55.6 ,
                      "worked_hrs": 6}
        
        Service.add(c2, s4_params)
        
        s5_params = {"replacement_part" : 'brakes',
                     "price_part": 132,
                     "worked_hrs": 12.33}
        Service.add(c2, s5_params)
        
        
        print 40 * '_-_'
        print Service.list(c).count()
        print 40 * '_-_'
        print Contact.list(g).count()
        
        print 20 * '-_-'
        
        price_part_price = 0
        worked_hrs = 0
        totall = 0
        
        for b in Service.list(c):
            if b.price_part:
                totall += price_part_price + b.price_part
#                 print "The %s will cost you : %d" % (b.replacement_part, b.price_part)
            if b.worked_hrs:
                worked_hrs = worked_hrs + b.worked_hrs
#                 print "Current work time is : %d hours " % worked_hrs
            if b.replacement_part:
#                 print "For %s was %d  hrs of work needed." % (b.replacement_part, b.worked_hrs)
    
                print 5 * '-'
#         totall += (worked_hrs * b.garage.price_per_hours) + b.price_part
#         print 'Total amount hours of work %s' % worked_hrs
#         print "Total price = %d" %
        
        currentgarage = c.garage.get()
        eindtotaal = worked_hrs * currentgarage.price_per_hours + totall
#         print "You need to pay %d " % eindtotaal
#         print 20 * '-_-'
        
#         for l in Service.query():
#             print l

        
        
#         print "\n"
#         print 15 * '='
#         print 'At Garage : %s \n ' % g.name 
#         print """You want to replace your %s . For the repair a total time of %d hours is needed, \n at a rate of %s per hour
#               this will let you pay %s golden coins in total .""" % (s1_params['replacement_part'], s1_params['worked_hrs'], g.price_per_hours, (s1_params['worked_hrs'] * g.price_per_hours) + s1_params['price_part']) 
#         print 15 * '='
#         print """And you want to have you car polished  . For the polishing service a total time of %d hours is needed, \n at a rate of %s per hour
#               this will let you pay %s golden coins in total .""" % (s2_params['worked_hrs'], g.price_per_hours, (s2_params['worked_hrs'] * g.price_per_hours)) 
#         print 15 * '='
#         print """And you also want to replace your %s . For the repair a total time of %d hours is needed, \n at a rate of %s per hour
#               this will let you pay %s golden coins in total .""" % (s3_params['replacement_part'], s3_params['worked_hrs'], g.price_per_hours, (s3_params['worked_hrs'] * g.price_per_hours) + s3_params['price_part']) 
#         print 15 * '='
#         print """
                 
        """
        logging.warning("The exact price is %s" % eindtotaal)
        logging.warning("Rounded price: %s" % round(eindtotaal))
        
    
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
                
        total = g.price_per_hours * s.worked_hrs +(s.price_part * 4)
        print "\n"
        print 15 * '=' 
        print 'At Garage : %s  \n ' % g.name
        print """
# You want to replace your %s . For the repair a total time of %d hours is needed, \n at a rate of %s per hour
#               this will let you pay %s golden coins in total. """ % (s.replacement_part, s.worked_hrs, g.price_per_hours, math.ceil(total) )
#         print 15 * '='
#         print " \n"
#          
#         total = g1.price_per_hours * s.worked_hrs +(s.price_part * 4)
#         print "\n"
#         print 15 * '=' 
#         print 'At Garage : %s  \n ' % g1.name
#         print """You want to replace your %s . For the repair a total time of %d hours is needed, \n at a rate of %s per hour
#               this will let you pay %s golden coins in total. """ % (s.replacement_part, s.worked_hrs, g1.price_per_hours, math.ceil(total) )
#         print 15 * '='
#         print " \n"
#                
#         for g2 in Garage.query():
#             print g2.name +" %s $: You will pay. Damn thats alot of cash.   " % g2.price_per_hours
#        self.assertEqual(2, Garage.query().count())
    
    def kljtest_new(self):
        
        garage1 = Garage(name='dummie garage',
                         brand='Toyota',
                         note='Closed',
                         price_per_hours=56,
                         roundup_workhrs=True)
        gkey = garage1.put()
        
        garage2 = Garage (name='ZupaDupa',
                           brand='Porsche',
                           note='Open',
                           price_per_hours=44.3,
                           roundup_workhrs=False)
        g2key = garage2.put()
        
        
        car1 = Car(name='Fastcar101',
                    brand='Toyota',
                    garage=garage1.key)
        c1key = car1.put()
        
        car2 = Car(name='RX493',
                   brand='Suzuki',
                   garage=garage1.key)
        c2key = car2.put()
        
        car3 = Car(name='RL4402',
                    brand='Fiat',
                    garage=garage2.key)
        c3key = car3.put(
                         )
        serv1 = Service(replacement_part='Chair',
                        price_part=4.53,
                        worked_hrs=4.0,
                        parent=car2.key
                        )
        serv1_key = serv1.put()
        
        serv2 = Service (replacement_part='Roof',
                         price_part=7897.95,
                         worked_hrs=21,
                         parent=car2.key)
        serv2.put()
        
        serv3 = Service(worked_hrs=45,
                         parent=car1.key
                         )
        serv3_key = serv3.put()
        
        serv4 = { "replacement_part" : 'Clotch',
                  "price_part" : 878,
                  "worked_hrs" : 12
                 }
        sk = Service.add(car1, serv4)
        par_name = sk.key.parent()
        logging.warning("par name = " + str(par_name))
        tst = par_name.get()
        print tst.name
        
        
        contact1 = Contact(name='Piet Jan',
                            email='sample@example.nl',
                            tel_nr='0314324886',
                            parent=c2key)
        contact1_key = contact1.put()
        
        contact2 = Contact(name='Floris',
                            email='Sample@upc.nl',
                            tel_nr='0254445987',
                            parent=c3key)
        contact2_key = contact2.put()
        
        
        
        rev_test = serv1_key.parent()
        # Retrieve the entitity
        test_garage = gkey.get()
        test_car1 = c1key.get()
        test_car2 = c2key.get()
        
        # Retrieve the kind from a key
        kindstring = gkey.kind()
        # Retrieve the ident from a key
        ident = gkey.id()
        
        
        
        
        
        print 30 * '___-___'
        print contact2_key
        print 30 * '___-___'
        print contact1_key
        print 40 * '-o-'
#         print rev_test2
        print 40 * '0o0o0'
        print kindstring
        print ident
        print 40 * '0o0o0'
        print 5 * '\n'
        print '--------------------------------------<><><><><>--------------------'
        print 'this is %s' % car1
        print "\n"
        print garage1
        print '\n'
        print test_car1
        print '\n'
        print test_car2
        print '\n'
        print test_garage
        print '\n'
        print '\n'
        print rev_test
        print 50 * '<><><><>||'
        
        
    def create_garage(self, data):
        return Garage.add(data)
    
    def create_car(self, garage, data):
        return Car.add(garage, data)
    
    def create_service(self, car, data):
        Service.add(car, data)
    
    def create_contact(self, car, data):
        Contact.add(car, data)
        
    def test_01(self):
        # New Garage #1
        g = self.create_garage({"name": "GarageDubi", "brand": "Porsche", "price_per_hours": 12})
        # New Car #1.1
        c = self.create_car(g, {"name": "FastName", "brand": "Nissan"})
        # New Contact #1.1.1
        self.create_contact(c, {"name": "Jean Paul", "email": "test@test.nl", "tel_nr": "0314-3233234"})
        # New Service #1.1.1
        self.create_service(c, {"replacement_part": 'Windows', "price_part": 18, "worked_hrs":12})
        # New Service #1.1.2
        self.create_service(c, {"replacement_part": 'Ashtray', "price_part": 200, "worked_hrs":7.9})
        print "Garage 1 auto 1"
        # Calculate Costs
        self.assertEqual(456.8, Car.calculate3(c))

        
        
        # New Car #1.2
        c = self.create_car(g, {"name": "SlowName", "brand": "Mazda"})
        # New Contract #1.2.1
        self.create_contact(c, {"name": "peter", "email" : "sample@sample.nl"})
        # New Service #1.2.1
        self.create_service(c, {"replacement_part": "YourGrandma", "price_part": 1566, "worked_hrs":156})
        # New Service #1.2.2
        self.create_service(c, {"replacement_part": "Oil", "price_part":548, "worked_hrs":12})
        # New Service #1.2.3
        self.create_service(c, {"worked_hrs": 1213})
        print "Garage 1 auto 2"        
        # Calculate Costs
        self.assertEqual(18686, Car.calculate3(c))
        
        # New Garage #2
        g = self.create_garage({"name": "GarageFlut", "brand": "Nissan", "price_per_hours": 15})
        # New Car #2.1
        c = self.create_car(g, {"name": 'BlingBling2000', "brand" : "Suzuki"})
        # New Contact #2.1.1         
        self.create_contact(c, {"name": "Mark", "email": "testing@test.nl", "tel_nr": "070-22332225"})
        # New Service #2.1.1
        self.create_service(c, {"replacement_part": "Brakes", "price_part": 122, "worked_hrs":34})
        # New Service #2.1.2
        self.create_service(c, {"replacement_part": "Chip-Tune_RD664570", "price_part": 215, "worked_hrs":17.2})
        print "Garage 2 auto 1"        
        # Calculate costs
        self.assertEqual(1105, Car.calculate3(c))
        
        # New Garage 3
        g = self.create_garage({"name": "HydroTune", "brand": "Ford", "price_per_hours": 7.5})
        # New Car 3.1
        c = self.create_car(g, {"name": 'ZingZagius', "brand" : "ZZ-Tupi"})
        # New Contact 3.1.1
        self.create_contact(c, {"name": "Kevin", "email": "kevin@test.nl", "tel_nr": "070-454654878"})
        # New Service 3.1.1
        self.create_service(c, {"replacement_part": "Brakes", "price_part": 46, "worked_hrs": 8})
        # New Service 3.1.2
        self.create_service(c, {"replacement_part": "Clutch", "price_part": 400, "worked_hrs": 18})
        print "Garage 3 auto 1"        
        # Calculate costs
        self.assertEqual(641, Car.calculate3(c))
        
        g = None
        c = None
        
#         for k in Garage.list():
#             for x in Car.list(k):
#                 for p in Service.list(x):
#                     if p.price_part:
#                         print Car.calculate(x, p.worked_hrs, k.price_per_hours, p.price_part)
#                     else:
#                         print Car.calculate(x, p.worked_hrs, k.price_per_hours)
                               
#         print "length of the Garage list :" 
#         print len(Garage.list())
        
#         ar = []
#         for k in Garage.list():
#             print "Garage naam:"
#             print k.name 
# 
#             
#             print "amount cars in Garage : [ %s ]" % k.name
#             print len(Car.list(k))
#             print '\n'
#             for x in Car.list(k):
#                 print "Name car :"
#                 print "%s is registered at garage %s with key %s " % (x.name,k.name,x.key)
#                 for p in Service.list(x):
#                     if p.price_part:
#                         print "Test = " + str(p.price_part)
#                         ar.append((k.price_per_hours * p.worked_hrs) + p.price_part)
#                     else:
#                         ar.append(k.price_per_hours * p.worked_hrs) 
#                     print "Work at car : %s " % x.name
#                     print p #printing services
#                     print '\n'
#             print "array :"
#             counter = 0
#             for xz in ar:
#                 counter = counter + 1
#                 print "bedrag %s is %s" % (counter, xz)        
        
        
#     def test_calc(self):
#         Car.calculate2(self)
        
    def tearDown(self):
        """ tearDown will be called after a testcase
        """
        pass
