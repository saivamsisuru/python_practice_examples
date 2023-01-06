n=int(input("enter any number: "))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    fs=0
    for i in range(1,n):
        if(n%i==0):
            print(i)
            fs=fs+i
    else:
        print("sum of factors are {}".format(fs))


