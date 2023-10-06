class Person:
    def __init__(self):
        # public 
        self.name="Ram"
        # protcted
        self._age=12
        # private
        self.__phone_number="987654323489"
    
    @property
    def phone_number(self):
        return self.__phone_number
    
    @phone_number.setter
    def phone_number(self,phone_number):
        self.__phone_number = phone_number
        
    # phone_number=property(get_phone_number,set_phone_number)
        
        
p=Person()
# yesma error private varibale cannot be access


# p.set_phone_number("1234567")
p.phone_number="33222552S"
print(p.phone_number)

# print(p.get_phone_number())


# 

