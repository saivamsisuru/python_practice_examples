#program to count the number of elements in a list within a specified range
count=0
lst=[int(val) for val in input().split()]
slist=[]
slist=lst.copy()
for x in lst:

        if(x in slist):
            count+=1
        else:
            continue
print(count)