n=int(input())
if n>9:
    print("неверное число")
else:
    for i in range(n):
        for a in range(1, i + 2):
            print(a, end='')
        print()