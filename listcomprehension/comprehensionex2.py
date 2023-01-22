#program for demonstrating set comprehension
lst={2,3,4,5,6,7,8,9,10}
slist={val**2 for val in lst }   #-----------set
print("original set",lst)
print("square set of the given set",slist)
