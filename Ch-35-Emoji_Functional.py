import math
import matplotlib
import string
import dataclasses
import importlib
import random
import string


if __name__ == "__main__":
    print("Running as Standalone, Taking Input")
    print("here any initialization / input as a standalone program is to be inputted")

    def Converter(InS:str):
        output = ""
        Emojis = {
            ":)": "😀",
            ":(": "😥",
            "XD": "😆"
        }
        LIns = InS.split(" ")
        for word in LIns:
            output += Emojis.get(word, word) + " "
        return output


    InS=input(">")
    print(Converter(InS))




else:
    print(f"Running as a module of another script, whose '__name__' = {__name__} , Not Taking input, Tyring to take parameterized input")

