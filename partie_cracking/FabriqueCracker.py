
from CrackerBrutForce import CrackerBrutForce
from CrackerDictionnary import CrackerDictionnary

class FabriqueCracker:
    
    def __init__(self):
        pass
    
    @staticmethod
    def get_instance(cracking_choice:int):
        if(cracking_choice == 1):
            return CrackerBrutForce()
        else:
            return CrackerDictionnary()
        
    
    