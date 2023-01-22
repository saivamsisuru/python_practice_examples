#program for demonstrating non list comprehension
lst=[2,3,4,5,6,7,8,9,10]
slist=[]
for val in lst:
    slist.append(val**2)
print("squares for the given list")
print(slist)
