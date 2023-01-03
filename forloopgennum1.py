#program for generating even numbers within n by using for loop
n=int(input("enter any number: "))
if(n<=0):
    print("{} is invalid input".format(n))

else:
    print("="*50)
    print("even numbers within {}".format(n))
    for i in range(2,n+1,2):
        print(i)