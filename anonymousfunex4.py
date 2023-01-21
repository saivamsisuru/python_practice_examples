#program for accepting list of names and sort the names in ascending order by anonymous functions

def readvalues():
    lst=[]
    n=int(input("enter how many number of values u want: "))
    if(n<=0):
        return lst
    else:
        for i in range(1,n+1):
            value=input("enter values for list: ")
            lst.append(value)
        return lst

sort=lambda lst:sorted(lst)

res1=readvalues()
res2=sort(res1)
print(res2)