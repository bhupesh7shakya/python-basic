import os

import time

try:
    f=open('hello.txt','a')
    # print(f.read(3))
    for i in range(11):
        f.write(f"{i+1} hello world\n")
    f.close()
    time.sleep(3)
    os.remove('hello.txt')
 
except FileNotFoundError:
    print("File Not found")
except:
    print("Somthing went wrong")
    
# task for today homework
# provide user with choices like create append, overide or delete a file 
# ask input for the user to create a txt file 
# also ask user for the content to write inside the file
# also ask your if you want to overide or append
# and also for delete a specific file 
