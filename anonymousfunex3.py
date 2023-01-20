#program for finding highest and smallest value from list of values by using anonymous functions
def readvalues():
    lst=[]
    n=int(input("enter how many number of values u want: "))
    if(n<=0):
        return lst
    else:
        for i in range(1,n+1):
            value=int(input("enter values for list"))
            lst.append(value)
        return lst


high=lambda lst:max(lst)
small=lambda lst:min(lst)

#main program
lst=readvalues()
if(len(lst)==0):
    print("given list is empty")
elif(len(set(lst))==1):
    print("max({})={}".format(lst, "ALL VALUES ARE EQUAL"))
    print("min({})={}".format(lst, "ALL VALUES ARE EQUAL"))
else:
    res1=high(lst)
    print("\t{} is higher in the list {}".format(res1,lst))
    res2=small(lst)
    print("\t{} is smaller than list{}".format(res2,lst))