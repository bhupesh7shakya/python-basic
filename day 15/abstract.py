from abc import ABC,abstractmethod

class Computer(ABC):
    
    @abstractmethod
    def process(self,app):
        pass
    
    def run(self,app):
        self.process(app)
    
class Laptop(Computer):
    def process(self,app):
        print(f"{app} Processing using laptop")

class Mobile(Computer):
    def process(self,app):
        print(f"{app} Processing using laptop")
    


dell=Laptop()
dell.run("Chrome")
dell.run("Pubg")


samsung=Mobile()
samsung.run("camera")
samsung.run("pubg")
