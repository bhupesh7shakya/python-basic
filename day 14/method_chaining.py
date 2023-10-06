class Burger:
    
    def bun(self):
        print("dough")
        return self
        
    def cheese(self):
        print("cheese")
        return self
        
        
    def chicken(self):
        print("chicken")
        return self
        
        
burger=Burger()

burger.bun() \
        .cheese()  \
        .chicken() \
        .bun()



