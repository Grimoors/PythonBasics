import math
import matplotlib
import string
import dataclasses
import importlib

if __name__ == "__main__":
    print("Running as Standalone, Taking Input")
    print("here any initialization / input as a standalone program is to be inputted")
else:
    print(f"Running as a module of another script, whose '__name__' = {__name__} , Not Taking input, Tyring to tkae parameterized input")

print("The Price of a swanky villa in San Francisco, CA = $1 million")


while True:
    _is_Credit_Good = input("Is your Credit Score sesky and awesome? (Y/N) {and don't bother Lying Mi Amigo} :")

    if ((_is_Credit_Good=='y')|(_is_Credit_Good=='Y')):
        print(f'Sweet , lad, you gotta gimme 10% of $1 milly, ie. ${0.1 * 1000000} as Downies')
        break
    elif ((_is_Credit_Good=='n')|(_is_Credit_Good=='N')):
        print(f'Sweet , lad, you gotta gimme 20% of $1 milly, ie. ${0.2 * 1000000} as Downies')
        break
    else:
        print(" Lad, Yes(y) or No(n)")

