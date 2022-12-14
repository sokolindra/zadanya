def f(a,b):
    dlina,x = 0, 0
    for i in range(a,b + 1):
        d = len([True for j in range(1, i) if i % j == 0])
        if d >= dlina and i > x:
            dlina, x = d, i
    return x


A = int(input('A: '))
B = int(input('B: '))
c=f(A,B)
print("ответ : ",c)








