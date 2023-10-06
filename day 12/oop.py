class House:

    
    def __init__(self,name,color="red",garden=True,window=10):
        self.name=name
        self.color=color
        self.garden=garden
        self.window=window
        
    def set_color(self,color):
        self.color=color
        
    
    def __eq__(self, object) -> bool:
        return self.color == object.color
    
    def __str__(self) :
        return f"{self.name} ko ho ra yestko color {self.color} ho"
    
ram_ko_ghar=House("ram","yellow",window=100)

print(ram_ko_ghar)
shyam_ko_ghar=House("shyam","black",window=10)

print(shyam_ko_ghar.__eq__(ram_ko_ghar))
# print(ram_ko_ghar.color)
# print(ram_ko_ghar.garden)

# shyam_ko_ghar=House()
# shyam_ko_ghar.set_color("green")
# print(type(shyam_ko_ghar))

# print(type(1))
# print(type("hello"))
# print(type(1.2))
# print(type([1,2,34]))

