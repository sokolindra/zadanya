n = int(input("введите кол-во минут"))
hours = n % (60 * 24) // 60
minutes = n % 60
print(hours, ":", minutes)