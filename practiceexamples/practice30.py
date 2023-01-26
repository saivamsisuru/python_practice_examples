#program to get the frequency of the elements in a list

#get the frequency of the elements in a list by using normal function
lst=[x for x in input().split()]
def frequency(lst):
    d={}
    for i in lst:
        if(i not in d):
            d[i]=1
        else: 
            d[i]=d.get(i)+1
    print(d,type(d))

frequency(lst)


print("========================")
#get the frequency of the elements in a list by importing collections module or import counter functions from collections module
from collections import Counter as c
print(dict(c(lst)))
