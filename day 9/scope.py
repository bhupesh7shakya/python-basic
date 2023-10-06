# a=10

# def number():
#     global a
#     a=11
#     print(a)
    
# number()
# print(a)

x=10
def outer():
    x=11
    def inner():
        global x
        x=12
        return x
    print(x)
    print(inner())


print(x)
outer()       