from random import randint
file = open(r"D:\git Norin\Norin_U-224_vvod1.txt",encoding='utf-8')
vvod= open(r"D:\git Norin\Norin_U-224_vvod1.txt",encoding='utf-8')
vivod= open(r"D:\git Norin\Norin_U-224_vivod1.txt",'w+',encoding='utf-8')
m=int(vvod.readline())
l = [[randint(-10, 10) for j in range(5)] for i in range(5)]
print(*l, sep='\n')
print()
for row in l:
    vivod.write(' '.join([str(l) for l in row]) + '\n')
x = []
for i in range(len(l)):
    x.append(l[i][i])
vivod.write("изменено:  ")
maxid = x.index(max(x))
l[maxid], l[m] = l[m], l[maxid]
print(*l, sep='\n')
for row in l:
    vivod.write(' '.join([str(l) for l in row]) + '\n')