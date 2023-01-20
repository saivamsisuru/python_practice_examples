#program for calculating factorial of a given number by using function
def fact():
    n=int(input("enter any number: "))
    fs=1
    for i in range(1,n+1):
        fs=fs*i
    print("factorial of {} = {}".format(n,fs))
fact()


