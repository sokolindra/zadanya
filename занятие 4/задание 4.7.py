n = int(input())
sum= 1
a= 1
for i in range(2, n + 1):
    a *= i
    sum+= a
print(sum)
