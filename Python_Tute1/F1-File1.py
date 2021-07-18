if __name__ == "__main__":
    print("Running as Standalone, Taking Input")
    print("here any initialization / input as a standalone program is to be inputted")


    #BASICS
    a = 5
    b = 10
    print (a+b)
    c= "LOL"
    #rint ( a + b + c )


    #TypeCasting
    print(str(a+b)+c)
    print("TheSumIs",str(a+b),c)

    # #Input
    # d = input("Daal naaaaaa")
    # #NOTE THIS
    # d=float(d)
    # d = int(d)
    # print(d)
    # print(type(d))

    # LISTS
    a=[]
    a.append("1")
    a.append(609)
    a.append([])

    print(a[0])
    print(type(a[0]))
    print(a)

    #problem with lists : Call by reference occurs

    b=a
    b[0] = 69
    print(a)

else:
    print(f"Running as a module of another script, whose '__name__' = {__name__} , Not Taking input, Tyring to take parameterized input")



