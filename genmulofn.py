#program for generating multiples of n by using for loop
n=int(input("enter a number: "))
m=int(input("enter no of the last number u need the multiples of n : "))
for i in range(n,m+1,n):
    print("no of multiples of {} below {} are {}".format(n,m,i))