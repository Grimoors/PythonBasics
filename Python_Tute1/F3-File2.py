import math
import matplotlib
import string
import dataclasses
import importlib
import random
import copy

if __name__ == "__main__":
    print("Running as Standalone, Taking Input")
    print("here any initialization / input as a standalone program is to be inputted")

    a=[]
    a.append(1)
    a.append("hello")
    a.append([1,"hello"])
    b=copy.copy(a)
    b[0]=69

    print(a)
    print((b))

else:
    print(f"Running as a module of another script, whose '__name__' = {__name__} , Not Taking input, Tyring to take parameterized input")

