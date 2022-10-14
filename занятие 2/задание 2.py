import math
x=float(input("x"))
y=float(input("y"))
z=float(input("z"))
s=float(2*math.cos(x-(2/3))/((0.5)+(math.sin(y))**2)*(1+((z**2)/(3-(z**2/5)))))
print("Ответ:",s)