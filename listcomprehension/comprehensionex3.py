#program for demonstrating list comprehension
lst=[2,3,4,5,6,7,8,9,10]
slist=(val**2 for val in lst )   #-----------generator
tpl=tuple(slist)  #------converting generator into tuple
print("original list",lst)
print("square list of the given list",tpl)

#               OR          #
"""
#program for demonstrating list comprehension
lst=[2,3,4,5,6,7,8,9,10]
slist=tuple(val**2 for val in lst )   #-----------generator----converting generator into tuple
print("original list",lst)
print("square list of the given list",slist)

"""