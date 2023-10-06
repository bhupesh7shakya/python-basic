while True:
    try:
        a=int(input('First number:'))
        b=int(input('Second number:'))
        print(a<b)
        if a<10:
            raise Exception("First number should alway greater then b!!!")
        print(a/b)
    
    
    
    except ZeroDivisionError:
        print("Zero number cannot be divided  ")
    except ValueError:
        print("Invalid input!! only accpt integer value")
    except:
        print("Something went wrong!Not valid input") 