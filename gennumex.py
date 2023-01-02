#program for generating 1 to n numbers where n is +ve integer value
n=int(input("enter a number: "))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    print("-"*50)
    print("Numbers within:{}".format(n))
    print("-"*50)
    i=1
    while(i<=n):
        print(i)
        i=i+1
    else:
        print("*"*50)
    print("program execution completed--while..else..cond")
print("program execution completed --if..else..cond")