from dataclasses import dataclass

@dataclass
class User:
    name : str = "Pa-Alioune"
    passwd : str = ""
    
    def login(self, passwd:str):
        return (self.passwd == passwd)
    
    