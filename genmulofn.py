#program for generating multiples pf 3 by using for loop
#display 10 multiples of n
n=int(input("enter a number: "))
m=int(input("enter no of the last number u need the multiples of n : "))
for i in range(n,m+1,n):
    print("multiples of {} are {}".format(n,i))