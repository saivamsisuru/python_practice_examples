#program to convert a list of characters into a string
import functools
lst=[ch for ch in input().split()]
print("".join(lst))
#by using reduce function
print("==============by using reduce function===========")
res=(functools.reduce(lambda a,b:a+b ,lst))
print(res,type(res))