#If- Else Statements

is_Hot=True
is_Cold=False

while True:
    hawt = input("\nIs it a Hot day? (y/n) : ")
    if ((hawt=='y')|(hawt=='Y')):
        is_Hot=True
        break
    elif ((hawt=='n')|(hawt=='N')):
        is_Hot=False
        break
    else:
        print("\nInput Y or N please UwU")

while (is_Hot == False):
    kewl = input("\nIs it a Cold day? (y/n) : ")
    if ((kewl=='y')|(kewl=='Y')):
        is_Cold=True
        break
    elif ((kewl=='n')|(kewl=='N')):
        is_Cold=False
        break
    else:
        print("\nInput Y or N please UwU")


if is_Hot:
    print("It's a Hot 😏😏(sxy) Day")
    print("Drink Plenty of water , You don't wanna be dehydrated 😏😏😏😏")
elif is_Cold:
    print("Its a cold day, Go warm up with your boooo 😘😘")
    print("cuddle dayyyy")
else:
    print("It's a lovely day today! Go do something amazing for yourself!!")
print("Enjoy Your Day")