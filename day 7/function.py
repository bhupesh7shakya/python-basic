# def hello(name,age,gender):
#     print(f'hello !!{name} your age is {age} , gender is {gender}')
    
# hello("Ram",gender='male',age=12,)
# hello("shyam")


# create a function name person
# # attribute name , age, gender , hobby list=[]
# # hobby one
# # hobby one
# # hobby one\
# #  

# def person(name,hobbies):
#     print(f'{name}')
#     for hobby in hobbies:
#         print(hobby)
        
# person('Ram',['coding','cycling','hiking'])


def person(**person):
    print(f"hello !!{person['name']} your age is {person['age']} , gender is {person['gender']}")

    
person(name="ram",age=12,gender="male")

# task
# simple calulator


