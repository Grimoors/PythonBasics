import math
import matplotlib
import string
import dataclasses
import importlib
import random


if __name__ == "__main__":
    print("Running as Standalone, Taking Input")
    print("here any initialization / input as a standalone program is to be inputted")
    matrixA=[
        [1, 2, 3],
        [2, 3, 4],
        [3, 4, 5]
    ]

    for rowi in matrixA:
        a=''
        for columnj in rowi:
            a=a+f"{columnj}"+' '
        print(a)

    print(matrixA)

    numbers=[5,6,7,8,9,10,11,12,13,14,15,16]
    numbers.append(420)
    print(numbers)
    numbers.insert(0,69)
    print(numbers)
    numbers.remove(5)
    print(numbers)
    numbers.pop()
    print(numbers)
    print(numbers.index(69))
    print(50 in numbers)
    print(numbers.count(5))
    print(numbers.sort(reverse=True))
    print(numbers)
    numbers2 = numbers.copy()
    print(numbers2)

    for i in numbers:
        numbers2.append(i)
    print(numbers2)

    for i in numbers2:
        if(numbers2.count(i)>1):
            numbers2.remove(i)
    print(numbers2)

    for i in numbers:
        numbers2.append(i)
    print(numbers2)

    uniqNum2=[]
    for i in numbers2:
        if(i not in uniqNum2):
            uniqNum2.append(i)
    print(uniqNum2)

    numbers.clear()
    print(numbers)

else:
    print(f"Running as a module of another script, whose '__name__' = {__name__} , Not Taking input, Tyring to take parameterized input")

