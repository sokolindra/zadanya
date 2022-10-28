a=int(input("введите числа"))

i=0
x=a
g=0
while a!=0:
    i+=1
    a=int(input("введите числа"))
    if x<a:
        g+=1
    x=a
print(g)