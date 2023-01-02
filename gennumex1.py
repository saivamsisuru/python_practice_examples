#program for generating n to 1 numbers where n is +ve integer value
n=int(input("enter a number: "))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    print("-"*50)
    print("Numbers within:{}".format(n))
    print("-"*50)
    i=n
    while(i>=1):
        print(i)
        i=i-1
    else:
        print("*"*50)
    print("program execution completed--while..else..cond")
print("program execution completed --if..else..cond")