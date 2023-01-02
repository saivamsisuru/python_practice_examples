#program for displaying odd number from 1 to n
n=int(input("enter a number: "))
if(n<=0):
    print("entered input is invalid: ")
else:
    i=1
    while(i<=n):
        print(i)
        i=i+2
