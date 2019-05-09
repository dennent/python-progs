
import random


def d20():
    x = random.randint(1, 20)
    if x == 1:
        print("oh no thats a crit fail")

    if (x > 13) and (x < 20):
        print("Nice roll")
 
    if (x > 1) and (x < 5):
        print("wow that was close")
        
    if x == 20:
        print("wow that is a crit success")
        
    return x



while(1):
    x = input("press enter to roll: ")
    print(d20())
    

    

        

        


