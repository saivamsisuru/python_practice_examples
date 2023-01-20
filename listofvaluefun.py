#program for accepting list of values and displaying its values
def readlist():
    n=int(input("enter how many values u want: "))
    if(n<=0):
        lst=[]

    else:
        lst=[]
        for i in range(1,n+1):
            value=input("enter any value: ")
            lst.append(value)
    displaylist(lst)
def displaylist(lst):
    if(len(lst)==0):
        print("given list is empty list")
    else:
        print("list of elements are")
        for i in lst:
            print(i)
lst=readlist()

