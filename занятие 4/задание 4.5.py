n=int(input("введите натуральное число"))
i=1
s=[]
while i<=n:
    s.append(i**3)
    i+=1
print(sum(s))

