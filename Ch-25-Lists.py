import math
import matplotlib
import string
import dataclasses
import importlib
import random


if __name__ == "__main__":
    print("Running as Standalone, Taking Input")
    print("here any initialization / input as a standalone program is to be inputted")
    List1=['bob','gob', 'jeb', 'notch','steve','alex']
    print(List1[:])

    List2=[1,2,3,4,5,6,7,8,9,0,10,11,69,21]
    a=List2[0]
    for i in List2:
        if(a<i):
            a=i

    print(f"The value of the  largest element in the list is {a}")

else:
    print(f"Running as a module of another script, whose '__name__' = {__name__} , Not Taking input, Tyring to take parameterized input")

