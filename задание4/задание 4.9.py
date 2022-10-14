import math
n=int(input())
i=1
f=1
s=[]

while i<=n:
    f=((1+math.sqrt(5))**i-(1-math.sqrt(5))**i)/(2**i*math.sqrt(5))
    s.append(f)
    i+=1
print(sum(s))
