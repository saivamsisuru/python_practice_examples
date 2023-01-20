#program for accepting any numberical integer value and decide whether the given number is perfect
def perfect():
    n=int(input("enter any number: "))
    if(n<=0):
        print("{} is invalid".format(n))
    else:
        fs=0
        for i in range(1,n):
            if(n%i==0):
                fs=fs+i
        else:
            if(fs==n):
                print("{} is perfect number".format(n))
            else:
                print("{} is not perfect number".format(n))

perfect()