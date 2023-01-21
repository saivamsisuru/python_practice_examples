#program for displaying unique digit from the given numerical integer value

def removeduplicates(n):
    dlist=[]
    ulist=[]
    for i in n:
        if(i not in dlist):
            dlist.append(i)
        else:
            ulist.append(i)
    return dlist,ulist
#main program
n=str(int(input("enter a numerical integer value: ")))
dlist,ulist=removeduplicates(n)

if(len(dlist)==0):
    print("List is empty and No need to remove duplicates")
else:
    print("unique digits from the given numerical value")
    for val in dlist:
        if(val not in ulist):
            print("\t",val)







