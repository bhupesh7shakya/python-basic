user_list=[]
while True:
    name=input('name:')
    password=input('password:')


    user={
        'name':name,
        'password':password
    }

    user_list.append(user)
    print(user_list)