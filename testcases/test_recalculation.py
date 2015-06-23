""" Very simple example how to use the BasicTestCase
"""

from practice.model.car import Car
from practice.model.contact import Contact
from practice.model.garage import Garage
from practice.model.service import Service
from testcases import BasicTestCase
from practice.model.receit import Receit
import logging

class GarageTestCase(BasicTestCase):
    
    def setUP(self):
        ''' This method can be used to import or set up some data needed for every testcase
            
            no need to call super
        '''
        pass
    
    @classmethod
    def get_dict(cls, obj, fields=None):
        if not fields:
            model = obj.__class__
            fields = [x for x in model._properties.keys() if not x.startswith("_")]
        return {k: getattr(obj, k) for k in fields}
    
    service_part = "oil"
    service_partprice = 15
    service_workhours = 3
    
    g_data = {"name": "CorneAutoTuning",
          "brand": "Mustang",
          "note": "WeGotCars!YouGotMoney?",
          "price_per_hours": 46, "roundup_workhrs": True}
    
    c_data = {"name": "Firebird",
              "brand": "Mustang"}
    
    cc_data = {"name": "Pablo Escobar", 
               "email": "cola@google.nl", 
               "tel_nr": "03464645", "klootfactor": 45}
    
    s_data = {"replacement_part": service_part, 
              "price_part": service_partprice, "worked_hrs": service_workhours}
    
    count = 0
    
    def line(self):
        print 20 * '=-='
    def space(self):
        print '\n'
        
    def dbspace(self):
        print 2 * '\n'
    
    #adding Garage
    def test_01(self):
        self.count = self.count + 1
        self.line()
        self.space()
        print "Start Test 1, adding,editing and deleting garages"
        #creating garage 

        Garage.add(self.g_data)
        
        logging.warning ("Now we created 1 garage")
        self.dbspace()
        for item in Garage.list("CorneAutoTuning"):key = item.key.id()
        garage = Garage.get(int(key))

        self.assertEqual('CorneAutoTuning', garage.name, "The data does not correspond")
        
        #edit garage
        garage.name, garage.brand = "CorneTuningInc", "Buic"
        #save edit
        garage.save()
        
        for item in Garage.list("CorneTuningInc"):
            key = item.key.id()
            print item
        garage = Garage.get(int(key))
        
        self.assertEqual("CorneTuningInc", garage.name, "The data does not correspond")
        
        #garage delete
        garage.delete()
        logging.warning("Now the garage is deleted")
        
        #check if there are no more garages
        self.assertEqual(0, len(Garage.list('CorneTuningInc')), "error!")
        print 
        
        print "END TEST %s" % self.count

        
        self.dbspace()

    #adding cars
    def test_02(self):
        
        self.line()
        print "Start TEST 2 adding,editing,deleting cars" 
        self.space()
        
        #add garage
        Garage.add(self.g_data)
        
        #retrieve garage
        for g in Garage.list('CorneAutoTuning'):ident = g.key.id()
        garage = Garage.get(ident)
        
        #creating car
        self.c_data['garage'] = garage.key.id()
        Car.add( self.c_data)
        
        for c in Car.listtest(garage.key):
            ident = c.key.id()
        car = Car.get(ident)
        
        logging.warning("We created 1 Car")
        print car
        
        self.assertEqual('Firebird', car.name, "The data does not correspond")
        
        #edit car
        car.name, car.brand = 'WaterHawk', 'Hummer'
        car.save()
        
        for c in Car.listtest(car.garage, name="WaterHawk"):ident = c.key.id()
        car = Car.get(ident)
        
        logging.warning( "We edited 1 car" )
        print car
        
        #test edit
        self.assertEqual(car.name, 'WaterHawk', 'car name does not correspond')
        
        #delete car
        Car.delete(car)
        
        #test if the car is deleted
        self.assertEquals(0, len(Car.listtest(car.garage, name="WaterHawk")))
        
        logging.warning("Car Deleted!")
        self.space()
        print"End Test 2"    
        self.dbspace()

    def test_03(self):
        self.line()
        print "Start test 3 Adding,Editing and deleting Contacts"
        self.space()

        #retrieve car
        for g in Garage.list('CorneAutoTuning'):
            ident = g.key.id()
        garage = Garage.get(ident)
        #add Car
        self.c_data['garage'] = garage.key.id()
        Car.add(self.c_data)
        
        #retrieve ID from entity key
        for c in Car.listtest(garage.key):
            ident = c.key.id()
        #retrieve car
        car = Car.get(ident)
        #create new contact
        Contact.add(car, self.cc_data)
        
        logging.warning( "We created 1 contact" )
        for cc in Contact.list(car):
            ident = cc.key.id()
        contact = Contact.get(ident, car.key)
        
        #self.assertEquals(self.get_dict(contact), self.cc_data)
        self.assertEqual(1, len(Contact.list(car)))
        
        #edit Contact entity
        contact.name = "PietjeFokker"
        #store contact entity
        Contact.save(contact)
        for c in Contact.list(car):ident = c.key.id()
        contact = Contact.get(ident, car.key)
        
        self.assertEquals("PietjeFokker", contact.name)
        
        #delete contact entity
        Contact.delete(contact)

        #Check if there are no more Contact entitys in datastore
        self.assertEqual(0, len(Contact.list(car)))
        self.space()
        print "End Test 3"
        self.dbspace()

    def test_04(self):
        self.line()
        print "Start Test 4 Adding, Calcutating, Editing and Deleting Services"
        self.space()
        
        #retrieve the garage
        for g in Garage.list('CorneAutoTuning'):ident = g.key.id()
        garage = Garage.get(ident)
        #retrieve ID from entity key

        for c in Car.listtest(garage.key):ident = c.key.id()
        car = Car.get(ident)
        #create contact
        Contact.add(car, self.cc_data)
        #retrieve contact
        for cc in Contact.list(car):ident = cc.key.id()
        contact = Contact.get(ident, car.key)
       
        # add service
        Service.add(car, self.s_data)
        logging.warning( "We created 1 service" )
        
        self.assertEqual(1, len(Service.list(car)))

        for s in Service.list(car):ident = s.key.id()
        service = Service.get(ident, car.key)
        self.assertDictEqual(self.get_dict(service), self.s_data)
        
        #calculate service cost
        cost = car.calculate()
        
        logging.warning("Costs %s" % cost )
        
        self.assertEqual(cost.total, 84.15)
        
        #Edit service
        service.replacement_part,service.worked_hrs   = "Fueltank", 19
        #store edited entity
        Service.save(service)
        
        for s in Service.list(car, "Fueltank"):ident = s.key.id()
        service = Service.get(ident, car.key)
        logging.warning( "EDITED %s "  % service )
        
        # recalculate service cost
        total = car.calculate()
        self.assertEqual(total.total, 488.95)
        #delete service
        Service.delete(service)
        self.assertEqual(0, len(Service.list(car)))
        logging.warning("Service Deleted!")
        
        self.space()
        print "End Test 4"
        self.dbspace()
        
    def test_05(self):
        self.line()
        print "Start Test 5 Adding, Calculating, Editing, Deleting receits"
        self.space()
        
        
        for g in Garage.list('CorneAutoTuning'):ident = g.key.id()
        garage = Garage.get(ident)
        for c in Car.listtest(garage.key):ident = c.key.id()
        car = Car.get(ident)
        for contact in Contact.list(car):ident = contact.key.id()
        contact = Contact.get(ident, car.key)
        
        #create a service
        Service.add(car, self.s_data)
        for service in Service.list(car):ident = service.key.id()
        service = Service.get(ident, car.key)
        
        logging.warning( "Service added" )
        
        #check if the service is added
        self.assertEqual(1, len(Service.list(car)))
        
        logging.warning( "CALCULATING" )
        #calculate total for receit from service
        total = car.calculate()

        logging.warning( "Receit total = %s" % total )
        import datetime
        Receit.add(car, {'total': total.total, 'service': service.key, 'car': car.key, 'servicedate': str(datetime.datetime.now())})
        for r in Receit.list(contact, car, service):ident = r.key.id()
        receit = Receit.get(ident)
        
        #check if total corresponds with receit total
        self.assertEqual(84.15, receit.total)
        
        #delete receit
        Receit.delete(receit)
        print Receit.query().count()
        
        #check if the receit is deleted
        self.assertEqual(0,len(Receit.list(car.garage.get())))
        
        logging.warning( "Receit deleted" )
        self.space()
        print "End Test 5"
        self.dbspace()
        
    def test_06(self):
        self.line()
        print "Start Test 06, Calculating multiple services from a list then compare the result with a similar list with different service values "
        self.space()
        
        
        for g in Garage.list('CorneAutoTuning'):ident = g.key.id()
        garage = Garage.get(ident)
        Car.add({"name": "ZZType1", "brand": "Mustang", "garage": garage.key.id()})
        for c in Car.listtest(garage.key):ident = c.key.id()
        car = Car.get(ident)
        Contact.add(car, {"name": "Mister Ecco", "email": "Ecco@google.nl", "tel_nr": "03464645", "klootfactor": 5})
        for contact in Contact.list(car):ident = contact.key.id()
        contact = Contact.get(ident, car.key)
        
        Service.add(car, {"replacement_part": "paint job","price_part": 450, "worked_hrs": 7})
        Service.add(car, {"replacement_part": "Cleaning","price_part": 75, "worked_hrs": 2})
        Service.add(car, {"replacement_part": "Wheels","price_part": 150, "worked_hrs": 1})
        Service.add(car, {"replacement_part": "Chip Tune","price_part": 350, "worked_hrs": 3})
        ls = []
        
        for s in Service.list(car):
            ident = s.key.id()
            service = Service.get(ident, car.key)
#             Receit.add(contact, service) 
            total = car.calculate()
            
            ls.append(total.total)
            logging.warn(total.total)
        #check if the sum of receits correspond
        self.assertEqual(1541.85, total.total)
        
        #add new car
        Car.add({"name":"RX093", "brand":"Mustang", "garage": garage.key.id()})
        
        for c in Car.listtest(garage.key, name='RX093'):ident = c.key.id()
        car = Car.get(ident)
        
        #add a new contact with a different klootcactor
        Contact.add(car, {"name": "Mis. Echo", "email": "Echo@google.nl", "tel_nr": "03464645", "klootfactor": 10})
        for cc in Contact.list(car):ident = cc.key.id()
        contact = Contact.get(ident, car.key)
        
        #add some new services
        Service.add(car, {"replacement_part": "paint job","price_part": 450, "worked_hrs": 7})
        Service.add(car, {"replacement_part": "Cleaning","price_part": 75, "worked_hrs": 2})
        Service.add(car, {"replacement_part": "Wheels","price_part": 150, "worked_hrs": 1})
        Service.add(car, {"replacement_part": "Chip Tune","price_part": 350, "worked_hrs": 3})
        ls2 = []
        testlist = []
        ls3 = []
        
        for s in Service.list(car):
            ident = s.key.id()
            service = Service.get(ident, car.key)
            total = car.calculate()
            ls2.append(total.total)
            testlist.append(service)
        
        money = car.calculate1(testlist)
        self.assertGreater(sum(ls), sum(ls2))
        
        
        #FOUT!
        for s in Service.list(car, "Cleaning"):
            ident = s.key.id()
        service = Service.get(ident, car.key)
        
        logging.warning("Deleting 1 service")
        car.delete_service(service)
        
        for s in Service.list(car):
            ident = s.key.id()
            service = Service.get(ident, car.key)
            ls3.append(service)
        print "New total %s" % car.calculate1(ls3)
        
        self.space() 
        print "END Test 06"
        self.dbspace()