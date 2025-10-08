num=int(input("enter the number: "))
c=0
for i in range(2,num):
    if num%i==0:
        c=c+1
if c==0:
    print("prime number")
else:
    print("not a prime number")
