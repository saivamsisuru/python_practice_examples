#program for eliminating duplicate letters from accepted line of text

def removeduplicates(n):
    dlist=[]
    for i in n:
        if(i not in dlist):
            dlist.append(i)

    return dlist
#main program
n=input("enter a text: ")
dlist=removeduplicates(n)

if(len(dlist)==0):
    print("List is empty and No need to remove duplicates")
else:
    for val in dlist:
        print(val)
