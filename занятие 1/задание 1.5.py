text=input("введите строку")
n=[int(s) for s in text.split() if s.isdigit()]
b=n[0]
a=b+b**2+b**3+b**4+b**5
print(a)
