#program for generating 1 to n multiplication table where n is the positive number
n=int(input("enter the value of n: "))
if(n<1):
    print("invalid input")
else:
    for i in range(1,n+1):
            print("="*50)
            for num in range(1,11):
                print("{} x {} ={}".format(i,num,num*i))
    else:
        print("=" * 50)