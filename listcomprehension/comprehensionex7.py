#program for getting even and odd list from the given list by using list comprehension
def readvals():
    lst=[]
    n=int(input("enter how many vals u want: "))
    if(n<0):
        return lst
    else:
        for i in range(1,n+1):
            val=int(input("enter {} value".format(i)))
            lst.append(val)
        return lst
lst=readvals()
evenlist=[val for val in lst if(val>0) and val%2==0]
oddlist=[val for val in lst if val>0 and val%2!=0 ]
print(evenlist)
print(oddlist)