import math
import matplotlib
import string
import dataclasses
import importlib
import random


if __name__ == "__main__":
    print("Running as Standalone, Taking Input")
    print("here any initialization / input as a standalone program is to be inputted")
    try:
        class Point:
            def __init__(self,x,y):
                self.x=x
                self.y=y

            def move(self):
                print("Move")
            def draw(self):
                print("Draw")




        point1=Point(69,420)
        print(point1.x,point1.y)
        point1.draw()


    except ZeroDivisionError:
        print("Division by 0 is not allowed")
    except ArithmeticError:
        print("Check Math Equations")


else:
    print(f"Running as a module of another script, whose '__name__' = {__name__} , Not Taking input, Tyring to take parameterized input")


