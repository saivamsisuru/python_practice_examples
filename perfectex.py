#program for accepting any numerical positive number and decide whether the given number is perfect or not
n=int(input("enter any number: "))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    print("-"*50)
    print("factors of {}".format(n))
    print("-" * 50)
    fs = 0
    for i in range(1, n):
        if (n % i == 0):
            print(i)
            fs = fs + i
    else:
        print("-" * 50)
        print("sum of factors are {}".format(fs))
        print("-" * 50)
        if(fs==n):
            print("{} is PERFECT".format(n))
        else:
            print("{} is not a PERFECT".format(n))