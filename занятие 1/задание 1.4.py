seconds=int(input("введите секунды"))
a=seconds//86400
b=seconds%86400//3600
c=seconds%86400%3600//60
d=seconds%86400%3600%60
print(a,":",b,":",c,":",d)
