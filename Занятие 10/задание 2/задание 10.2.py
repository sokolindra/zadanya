file = open(r"D:\git Norin\Norin_U-224_vvod2.txt",encoding='utf-8')
vvod= open(r"D:\git Norin\Norin_U-224_vvod2.txt",encoding='utf-8')
vivod= open(r"D:\git Norin\Norin_U-224_vivod2.txt",'w+',encoding='utf-8')

N = int(vvod.readline())
a = [None] * N
for i in range(N): a[i] = [None] * N
x = 0
y = 0
dx = 1
dy = 0
for i in range(N * N):
    a[y][x] = i + 1
    test = x + dx if dx else y + dy
    if test < 0 or test == N or a[y + dy][x + dx] != None:
        dx, dy = -dy, dx
    x += dx
    y += dy

for y in range(N): print(a[y])
for row in a:
    vivod.write(' '.join([str(a) for a in row]) + '\n')