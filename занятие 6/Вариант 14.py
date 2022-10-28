s=input("введите строку")
g=s.split()
i=1
for i in range(0,len(g)):
    x=g[i]
    if x.find("а")==0 or x.find("А")==0:
        print(x)
    if x.find("я")==len(x)-1 or x.find("Я")==len(x)-1:
        print(x)





