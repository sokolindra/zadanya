spisok = input("введите числа")
l=spisok.split( )

for i in range(len(l)):
     l[i] = int(l[i])

x= max(l)
z= min(l)
f= l.index(max(l),0,-1)
g= l.index(min(l),0,-1)
l[f]=z
l[g]=x
print(l)