#function for printing multiplication table of the given number  
def Multable():
    n=int(input("enter the number to get the multiplication of the number: "))
    if(n<=0):
        print("you entered invalid input-try again")
    else:
        for i in range(1,11):
            print("{}  x  {} = {}".format(n,i,n*i))