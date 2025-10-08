a=()
l=[]
n=int(input("enter the limit: "))
for i in range(1,n+1):
            item=int(input("enter element: "))
            l.append(item)
a=a+tuple(l)
print(a)
