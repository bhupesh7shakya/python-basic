class GrandFather:
    def __init__(self):
        print(" Grandfather has luxery house")
        
    house="luxery house"

class Father(GrandFather):
    def __init__(self):
        print(" Father has 3bhk house")
        super().__init__()
    car="ferrari"

class Mother:
    jewellary="sun chadi..."

class Son(Father):
    def __init__(self):
        print("Son has  bought 2 houses")
        super().__init__()

    electronics="PS5"
    
son = Son()

father=Father()

son
# print(isinstance(son,object))


# print(son.jewellary)
# print(son.car)
# print(son.house)


