#program for eliminating duplicate values from the given list

def readvalues():
    lst=[]
    n=int(input("enter how many number of values u want: "))
    if(n<=0):
        return lst
    else:
        for i in range(1,n+1):
            value=int(input("enter values for list: "))
            lst.append(value)
        return lst
def removeduplicates(lst):
    dlst = []  # [10
    for val in lst:
        if val not in dlst:
            dlst.append(val)
    else:
        return dlst

#main program
lst=readvalues()
if(len(lst)==0):
    print("List is empty and No need to remove duplicates")
else:
    unqlist=removeduplicates(lst)
    print("Given List with Unique and Duplicates={}".format(lst))
    print("List with Unique={}".format(unqlist))