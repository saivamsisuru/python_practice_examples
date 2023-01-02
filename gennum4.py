#program for generating multiplicaqtion table for given +ve integer value
n=int(input("enter a number: "))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    print("-"*50)
    print("multiplication for given number{}".format(n))
    print("-"*50)
    i=1
    while(i<=10):
        print("\t {} x {} = {}".format(n,i,n*i))
        i=i+1
    else:
        print("*"*50)
    print("program execution completed--while..else..cond")
print("program execution completed --if..else..cond")