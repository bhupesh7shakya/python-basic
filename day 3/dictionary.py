# person

persons=[
    {
        'name':'Ram',
        'age':12,
        'gender':'male',
        'langages':[
            'python','java'
        ],
        # family member key tuple person name , relation
    },
    {
        'name':'shyam',
        'age':12,
        'gender':'male',
        'langages':[
            'python','java'
        ]
    },
    {
        'name':'hari',
        'age':12,
        'gender':'male',
        'langages':[
            'python','java'
        ]
    },
         
         
]

# alt+shift+down arrow key

print(f"""
My name is {persons[0]['name']}
and age is  {persons[0]['age']}
and gender is  {persons[0]['age']}
and i Know  differnet languages like
    1. {persons[0]['langages'][0]}
    2. {persons[0]['langages'][1][1::]}

""")

# ctrl+d
print(f"""
My name is {persons[1]['name']}
and age is  {persons[1]['age']}
and gender is  {persons[1]['age']}
and i Know  differnet languages like
    1. {persons[1]['langages'][0]}
    2. {persons[1]['langages'][1][1::]}

""")

# print(type(person))
# print(person['name'])


# 
# name="test"
# age=10
# # my name is ____ and age is____
# print(f"My name is  {name} and age is{age}")