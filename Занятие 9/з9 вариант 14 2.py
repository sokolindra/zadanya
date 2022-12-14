N = 5
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