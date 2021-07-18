import math
import matplotlib
import string
import dataclasses
import importlib
import random

if __name__ == "__main__":
    print("Running as Standalone, Taking Input")
    print("here any initialization / input as a standalone program is to be inputted")
else:
    print(f"Running as a module of another script, whose '__name__' = {__name__} , Not Taking input, Tyring to take parameterized input")


while 1:
    print("There is a random number. It is <= 14 and >=1, in 3 categories, <7, =7, >7. Guess which one")
    print("input 69 to exit")
    count=0

    random_secret_number= int(random.randint(0, 14))

    while 1:


        x =int(input("Enter a number"))

        if(x==69):
            print("Force Quitting")
            break
        elif x==7 & random_secret_number ==7:
            print("You win, the secret no was 7")
            break
        elif x<7 & random_secret_number <7:
            print("You win, the secret no was < 7")
            break
        elif x>7 & random_secret_number >7:
            print("You win, the secret no was > 7")
            break
        else:
            print('Try again')
            count += 1
            if(count==3):
                print(f"You failed thrice, too bad, The answer was {random_secret_number}")
                break
    continueq=input("Would you like to continue? press n to exit")
    if (continueq)=='n':
        break