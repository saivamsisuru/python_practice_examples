#program for generating factorial of a given number
n=int(input("enter a number: "))
rs=1
i=1
for i in range(1,n):
    rs=rs*i
    i=i+1
else:
    print("factorial of {} is {}".format(i,rs*i))