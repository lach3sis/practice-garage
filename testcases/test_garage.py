from testcases.base import BasicTestCase
from practice.model.garage import Garage


class Test_case1(BasicTestCase):
    @classmethod
    def get_dict(cls, obj, fields=None):
        if not fields:
            model = obj.__class__
            fields = [x for x in model._properties.keys() if not x.startswith("_")]
        return {k: getattr(obj, k) for k in fields}

    def test_01(self):
        ''' 
        Adding, Editing, Deleting Garages
        '''
        Garage.add({"name": "TurboTune", "brand": "Porsche", "price_per_hours": 11, "note": "Wij zijn Dicht!"})
        self.assertEqual(1, len(Garage.list()), "No you suck")
        
        #editing Garage
        for g in  Garage.list("TurboTune"):
            ident = g.key.id()
        garage = Garage.get(ident)
        props = {"name": "TurboWave", "brand": "RUF"}
        Garage.update(garage.key.id(), props)
        self.assertEqual(1, len(Garage.list("TurboWave")))
        
        for item in Garage.list("TurboWave"):
            garage = item
        self.assertDictEqual(self.get_dict(garage, props.keys()), props)
        #.keys gives scope on Keywords from a dictionary
            
        #deleting garage      
        Garage.delete(garage)
        self.assertEqual(0, len(Garage.list()))            