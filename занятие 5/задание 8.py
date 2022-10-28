a=int(input("введите числа"))
i=0
x=a
g=1
s=[]
while a!=0:
    i+=1
    a=int(input("введите числа"))
    if x==a:
        g+=1
        s.append(g)
    else:
        g=1
        s.append(g)
    x=a
print(max(s))


