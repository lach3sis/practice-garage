from testcases.base.extended import ExtendedTestCase
from practice.model.car import Car


class Test_car(ExtendedTestCase):

    def setUP(self):
        
        ExtendedTestCase.setUP(self)

    def test_01(self):
        ''' Adding cars, editing, deleting and retrieving cars
        '''
        #Add a car
        garage = self.get_garage() 
        Car.add(garage, {"name": "Lightning", "brand": "Bugatti", "garage": garage.key})

        self.assertEqual(1, len(Car.listtest(garage, "Lightning")))
        Car.add(garage, {"name": "Vulcano", "brand": "Porsche", "garage": garage.key})
        self.assertEqual(2, len(Car.listtest(garage)))
        
        #Update a car
        car = None
        for c in Car.listtest(garage):
            if c.name == "Vulcano" :
                car = c
        props = {"name": "Tsunami", "brand": "Saab" }
        self.assertFalse(car is None, "Car Vulcano not found")
        Car.update(car.key.id(), props)
        
        car = None
        for item in Car.listtest(garage=garage):
            if item.name == "Tsunami":
                car = item
        self.assertFalse(car is None, "Car Tsunami not found")        
        self.assertEqual("Tsunami", car.name, "names do not correspond")
        
        #Add a service via car
        props = {"replacement_part": "Paintjob", 
                "price_part": 500, "worked_hrs": 3}
        car.add_carservice(props)
        self.assertEqual(1, len(car.listservices()))
        
        Car.delete_contact(car)
        
        #testing adding contact to car
        props = {"name": "Drac Vladje", 
                          "email": "Vladje@dracul.com", 
                          "tel_nr": "065461125", 
                          "klootfactor": 666, 
                          "car": car.key}
        Car.add_carcontact(car, props)
        from practice.model.contact import Contact
        self.assertEqual(1, len(Contact.list(car)))
        self.assertEqual(1, len(Car.listcontact(car)))
        
        Car.delete_contact(car)
        self.assertEqual(0, len(Contact.list(car)))
        
        #Delete a service from a car
        from practice.model.service import Service
        for item in Car.listservices(car):ident = item.key.id()
        service = Service.get(ident, car.key)
        Car.delete_service(car, service)
        self.assertEqual(0, len(Car.listservices(car)))
        
        #Deleting a car
        Car.delete(car)
        self.assertEqual(1, len(Car.listtest(garage)), "there is either more or less than 1 car left")       