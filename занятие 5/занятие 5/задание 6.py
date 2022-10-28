a=int(input("введите числа"))

i=0
s=[]
s.append(a)
while a!=0:
    i+=1
    a=int(input("введите числа"))
    s.append(a)
print("среднее арифметическое=",sum(s)/i)

