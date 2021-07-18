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

    def func1(a:int,b:dict,c:list):
        print(a,b,c)
        return a,69,69,69,420

    func1("Yes","do it", "ONEGAIII")
    haha,a2,b2,c3,d4=func1("10",{"hello":"heyBabe"},[1,2,3,'d'])
    print(haha,a2,b2,c3,d4)

    #fun - Custom typecasters
    AAHAAH= int
    b= 5.1
    dfdf= AAHAAH(5.1)
    print(dfdf)

    #variable args
    def func2(a:int, b:dict,c:list,*args,**kwards):
        print(args)
        print ("args printed")
        print(kwards)
        print("kwargs printed")

    func2(56,23,123,123,123,123,123,12,3123)

    #default values
    def f3(a=[6060]):
        print(a)

        #kwargs is a dictionary with variable names as keys and the Values as values
        # If
        # we
        # supply
        # extra
        # arguments
        # like
        # -> "extra1", "extra2", f = 69, l33t = 420
        #
        # do
        # extra1 and 2
        # goto
        # the * args
        # and f and l33t
        # goes
        # into
        # kwargs




else:
    print(f"Running as a module of another script, whose '__name__' = {__name__} , Not Taking input, Tyring to take parameterized input")

