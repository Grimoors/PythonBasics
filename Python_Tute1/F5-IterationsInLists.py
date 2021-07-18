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


    for i in a:
        print (i)

    for i in range(3):
        print(a[i])

    for i, value in enumerate(a):
        print(str(i) + str(value))

    #range : for i in range(10)
    #== for ( int i=0;i<10;i++)
    #for i in range (1,10,0.5)
    # == for (int i = 1; i < 10; i+=0.5)

    # while cond:
    #     #     statements 1
    #     # else:
    #     #     statements 2

    # if cond:
    #     statements 1
    # elif cond2:
    #     statements 2
    # else:
    #     statements 3

    # if cond 1 and cond 2:
    #     if cond 3 | cond 4:
    #         if cond 6 == cond 5:
    #             print("kuch zyada ho gya")

    a=[1,2,3]
    print (1 in a)

    b = "My name is Vivek"
    print("name" in  b)
    b.find("name")







else:
    print(f"Running as a module of another script, whose '__name__' = {__name__} , Not Taking input, Tyring to take parameterized input")

