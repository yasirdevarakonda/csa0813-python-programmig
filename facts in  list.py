a=[]
b=[]
ch=input()
while ch=="y" or ch=="Y":
    item=int(input("element: "))
    a.append(item)
    ch=input()
for i in a:
    fact=1
    for j in range(1,i+1):
        fact = fact*j
    b.append(fact)
print(b)
