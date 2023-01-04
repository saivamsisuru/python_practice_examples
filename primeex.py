#program to check whether the given number is prime or not
n=int(input("enter any number: "))
if(n<=1):
    print("invalid input")
else:
    res=False
    for i in range(2,n):
        if(n%i==0):
            res=True
            break
    if(res==False):
        print("{} is a prime number".format(n))
    else:
        print("{} is not a prime number".format(n))

