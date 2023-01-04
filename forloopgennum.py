#program for generating odd numbers within n by using for loop
n=int(input("enter any number: "))
if(n<=0):
    print("{} is invalid input".format(n))

else:
    print("="*50)
    print("odd numbers within {}".format(n))
    for i in range(1,n+1,2):
        print(i)
