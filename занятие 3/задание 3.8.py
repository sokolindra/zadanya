
def f(a,b,c):
    if a == b == c:
        m=3
    elif a == b or b == c or a == c:
        m=2
    else:
        m=0
    return m

a = int(input())
b = int(input())
c = int(input())
k=f(a,b,c)
print(k)