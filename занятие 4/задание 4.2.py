a=int(input("a"))
b=int(input("b"))
if a==b:
    print("неправильно заданы числа")
elif a<b:
    while a<=b:
        print(a)
        a+=1
else:
    while a>=b:
        print(a)
        a-=1

