l = []

for i in range(10):
    l.append(float(input()))
x= sum(l)//len(l)

for i in range(len(l)):
    if l[i]>x:
        l[i]=1
print(l)
