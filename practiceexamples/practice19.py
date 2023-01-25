#program to get the difference between the two lists (in this program we have done difference from 1st list to 2nd list ))
lst1=[int(val) for val in input().split()]
lst2=[int(val) for val in input().split()]
#1st method
print(list((set(lst1)-set(lst2))))
print("===================")
#2nd method
lst3=[]
for x in lst1:
    if(x in lst2):
        continue
    else:
        lst3.append(x)
print(lst3)
print("===============")
#3rd method
lst4=[x for x in lst1 if x not in lst2]
print(lst4)