n=int(input("Enter the rows: "))
for i in range(1,n+1):
    space=(n-i)*" "
    pattren="* "*i
    print(space+pattren)
