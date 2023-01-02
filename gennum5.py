#program for generating sum of n natural numbers
n=int(input("enter a number: "))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    print("-"*50)
    print("-"*50)
    rs=0
    i=1
    while(i<=n):
        print(i)
        rs=rs+i
        i=i+1
    else:
        print("-" * 50)
        print("sum of {} natural numbers ={}".format(n,rs))
        print("*"*50)
    print("program execution completed--while..else..cond")
print("program execution completed --if..else..cond")