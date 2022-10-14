def f(a,b,c):
    if b >= a <= c:
        m=a
    elif a >= b <= c:
        m=b
    else:
        m=c
    return int(m)

a = float(input("введите первое число"))
b = float(input("введите второе число"))
c = float(input("введите третье число"))

k=f(a,b,c)
print(k)
