#program to check whether the given number is +ve or -ve by using if elif else
n=int(input("enter a number: "))
if (n==0):
    print("{} is Zero".format(n))
elif (n>0):
    print("{} is positive number".format(n))
elif (n<0):
    print("{} is negative number".format(n))
print("program execution completed")
