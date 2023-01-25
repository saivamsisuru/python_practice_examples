#program to flatten a shallow list
import itertools
val1=[x for x in input("enter values of val1").split()]
val2=[x for x in input("enter values of val2").split()]
val3=[x for x in input("enter values of val3").split()]
lst=[val1,val2,val3] 
#by using list comprehension
print([item for sublst in lst for item in sublst])
print("=================="*1)
#by using itertools.chain()
print(list(itertools.chain(*lst)))
print("=================="*1)
#by using nested for loop
lst1=[]
for sublst in lst:
    for item in sublst:
        lst1.append(item)
print(lst1)