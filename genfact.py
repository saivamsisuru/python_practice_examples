#program for generating factorial of a given number
n=int(input("enter a number: "))
rs=1
i=1
for i in range(1,n+1):  #(n,0,-1)
    rs=rs*i
else:
    print("factorial of {} is {}".format(n,rs))