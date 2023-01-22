#program for demonstrating list comprehension
lst=[2,3,4,5,6,7,8,9,10]
slist=dict([(val,val**2) for val in lst ])   #--------dict
print("original list",lst)
print("square list of the given list",slist)
for v,vs in slist.items():
    print(v,"----->",vs)