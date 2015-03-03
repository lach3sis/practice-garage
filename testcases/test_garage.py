'''
Created on Mar 2, 2015

@author: michaelroes
'''
from testcases.base import BasicTestCase
from practice.model.garage import Garage


class Test_case1(BasicTestCase):

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
            
        #deleting garage      
        Garage.delete(garage)
        self.assertEqual(0, len(Garage.list()))            