def f(s):
    a = 1
    for x in s:
        a = a * x
    return a

n=int(input())
i=1
s=[]

while i<=n:
    s.append(i)
    i+=1
print(f(s))

