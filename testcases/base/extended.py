from testcases.base.base import BasicTestCase
class ExtendedTestCase(BasicTestCase):
    def test_01(self):
        self.log("Harrrroo")

        
    def get_garage(self, name="TurboTune"):
        from practice.model.garage import Garage
        self.log(name)
        if len(Garage.list()) <= 0:
            props = {"name": "TurboTune", "brand": "Porsche", "price_per_hours": 11, "note": "Wij zijn Dicht!"}
            return Garage.add(props)
        else:
            for g in Garage.list():
                ident = g.key.id()
            garage = Garage.get(ident)
            return garage
        
    def get_car(self, name="Cheetah"):
        from practice.model.garage import Garage
        garage = self.get_garage(name)
                
        from practice.model.car import Car
        self.log(name)
        if len(Car.listtest(garage, "Cheetah")) <= 0 :
            props = {"name": "Cheetah", "brand": "Porsche", "garage": garage.key}
            return Car.add(garage, props)
        else:
            for c in Car.listtest(garage): ident = c.key.id()
            return Car.get(ident)

    def get_contact(self, name="Jan"):
        from practice.model.contact import Contact
        car = self.get_car()
        
        self.log(name)
        if len(Contact.list(car, "Jan")) <= 0 :
            props = {"name": "Jan", "email": "Jan@Jansen.com", "tel_nr": "065461125", "klootfactor": 7, "car": car.key}
            return Contact.add(car, props)
        else:
            for c in Contact.list(car, "Jan"):ident = c.key.id()
            return Contact.get(ident)
            
    def get_service(self,):
        pass