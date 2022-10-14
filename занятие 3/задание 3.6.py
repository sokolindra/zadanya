def f(a,b,c,d):
    if (x1 + y1 + x2 + y2) % 2 == 0:
        m="да"
    else:
        m="нет"
    return m

x1 = int(input("x1"))
y1 = int(input("y1"))
x2 = int(input("x2"))
y2 = int(input("y2"))

k=f(x1,y1,x2,y2)
print(k)
