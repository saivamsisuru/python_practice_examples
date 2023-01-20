#program for accepting numerical integer values and display its multiplication table by using functions
def multable():
    n=int(input("enter any number: "))
    if(n<=0):
        print("{} is an invalid input".format(n))
    else:
        print("multiplication table of {} ".format(n))
        for i in range(1,11):
            print("{} x {} ={}".format(n,i,n*i))
multable()