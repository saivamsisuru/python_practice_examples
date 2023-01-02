#program for displaying even number from 1 to n
n=int(input("enter a number: "))
if(n<=0):
    print("entered is invalid input")
else:
    i=2
    while(i<=n):
        print(i)
        i=i+2
    else:
        print("program execution is completed")