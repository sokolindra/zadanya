print("задание 1")
a=float(input("введите первое число"))
b=float(input("введите второе число"))
c=float(input("введите третье число"))
s=a+b+c
print("сумма",a,",",b,",",c,"=",s)
z=int(input("следующее задание?(1=да/0=нет)"))
if z==1:
    print("задание 2")
    a=float(input("введите длину первого катета"))
    b=float(input("введите длину второго катета"))
    s=0.5*a*b
    print("площадь треугольника равна",s)
    z = int(input("следующее задание?(1=да/0=нет)"))
    if z == 1:
        print("задание 3")
        n = int(input("введите кол-во минут"))
        hours = n % (60 * 24) // 60
        minutes = n % 60
        print(hours,":",minutes)
        z = int(input("следующее задание?(1=да/0=нет)"))
        if z == 1:
            print("задание 4, не решено")
            z = int(input("следующее задание?(1=да/0=нет)"))
            if z == 1:
                print("задание 5")
                a = float(input("введите первое число"))
                b = float(input("введите второе число"))
                c = float(input("введите третье число"))

                if b >= a <= c:
                    print(a)
                elif a >= b <= c:
                    print(b)
                else:
                    print(c)
                z = int(input("следующее задание?(1=да/0=нет)"))
                if z == 1:
                    print("задание 6")
                    x1 = int(input())
                    y1 = int(input())
                    x2 = int(input())
                    y2 = int(input())
                    if (x1 + y1 + x2 + y2) % 2 == 0:
                        print('Да')
                    else:
                        print('Нет')
                    z = int(input("следующее задание?(1=да/0=нет)"))
                    if z == 1:
                        print("задание 7")
                        year = int(input())
                        if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
                            print('Да')
                        else:
                            print('Нет')
                        z = int(input("следующее задание?(1=да/0=нет)"))
                        if z == 1:
                            print("задание 8")
                            a = int(input())
                            b = int(input())
                            c = int(input())
                            if a == b == c:
                                print(3)
                            elif a == b or b == c or a == c:
                                print(2)
                            else:
                                print(0)
                            z = int(input("следующее задание?(1=да/0=нет)"))
                            if z == 1:
                                print("задание 9")
                                n = int(input())
                                m = int(input())
                                k = int(input())
                                if k < n * m and ((k % n == 0) or (k % m == 0)):
                                    print('Да')
                                else:
                                    print('Нет')
                                print("конец задач")
                            else:print("конец")
                        else:print("конец")

                    else:print("конец")

                else:print("конец")

            else:print("конец")


        else:
            print("конец")


    else:
        print("конец")
else:print("конец")
