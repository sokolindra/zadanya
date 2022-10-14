
def f(a,b,c):
    if k < n * m and ((k % n == 0) or (k % m == 0)):
        j="да"
    else:
        j="нет"
    return j

n = int(input())
m = int(input())
k = int(input())
s=f(n,m,k)
print(s)