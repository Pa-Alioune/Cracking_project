from FabriqueCracker import FabriqueCracker

class PasswdCracker:
    
    def __init__(self):
        pass
    
    @staticmethod
    def cracker_passwd():
        print("Salut Pa-Alioune, ")
        print("Nous allons cracker le mot de passe de ton compte.")
        print("Comment veux-tu que nous nous y prenons ?\n")
        
        while True:
            print("1 : Par force brute  ⚔️")
            print("2 : Par dictionnaire 📖\n")
            cracking_choice = input("Ton choix 🤔 ? ")
            cracking_choice = int(cracking_choice)
            if (cracking_choice == 1 or cracking_choice == 2):
                cracker = FabriqueCracker.get_instance(cracking_choice)
                cracker.find_passwd()
                break
            
PasswdCracker.cracker_passwd()            
                
        
        