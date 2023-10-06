# def sum(a):
#     return a+10


# print(sum(10))

# sum=lambda a:a+10

# print(sum(10))


def myFunc(n):
    return lambda a:a*n


# lambda a:a*2
doubler =myFunc(2) 
# lambda a:a*3
tripler=myFunc(3)


# print(doubler(10))
print(tripler(3))
# four times