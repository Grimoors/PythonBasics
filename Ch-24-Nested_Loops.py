import math
import matplotlib
import string
import dataclasses
import importlib
import random


if __name__ == "__main__":
    print("Running as Standalone, Taking Input")
    print("here any initialization / input as a standalone program is to be inputted")

    for i in range(0,5,1):
        if(i==0)|(i==2):
            print("x"*5)
        else:
            print("x"*2)

else:
    print(f"Running as a module of another script, whose '__name__' = {__name__} , Not Taking input, Tyring to take parameterized input")
