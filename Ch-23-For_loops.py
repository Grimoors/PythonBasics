import math
import matplotlib
import string
import dataclasses
import importlib
import random


if __name__ == "__main__":
    print("Running as Standalone, Taking Input")
    print("here any initialization / input as a standalone program is to be inputted")

    for item in "AssAssIn's Creed ":
        print(item)

    for item in ["Nothing" ,"is" ,"true" ,"Everything" ,"is" ,"permitted"]:
        print(item)

    for item in [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9]:
        print("Tester" * item)

    x=1
    print("!^5 x == :-")
    for item in range(69 , 1 , -5):
        x *= item
        print(x)



else:
    print(f"Running as a module of another script, whose '__name__' = {__name__} , Not Taking input, Tyring to take parameterized input")

