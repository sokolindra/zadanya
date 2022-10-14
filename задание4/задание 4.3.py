a=int(input("a"))
b=int(input("b"))
if a<=b:
    print("неправильно заданы числа")
else:
    while a>=b:
        if a%2!=0:
            print(a)
        a-=1

