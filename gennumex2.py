#program for displaying odd number within n to 1
n=int(input("enter a number: "))
if(n<=0):
    print("entered input is invalid: ")
else:
    while(n>=1):
        if(n%2!=0):
            print(n)
        n=n-1
    else:
        print("program execution is completed")