
def f(a):
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        m="да"
    else:
        m="нет"
    return m
year = int(input())
k=f(year)
print(k)
