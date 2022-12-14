from random import randint

m = int(input("введите номер"))
l = [[randint(-10, 10) for j in range(5)] for i in range(5)]
print(*l, sep='\n')
print()

x = []
for i in range(len(l)):
    x.append(l[i][i])

maxid = x.index(max(x))
l[maxid], l[m] = l[m], l[maxid]
print(*l, sep='\n')