#program for adding the content of two list of objects
lst1=[int(val) for val in input().split()]
lst2=[int(val) for val in input().split()]
res=list(map(lambda val1,val2:val1+val2,lst1,lst2))
print(res)