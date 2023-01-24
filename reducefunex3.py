#program for accepting list of valued and find max and min by using reduce function
import functools
print("Enter List of Values separated by space for finding max and min:")
lst=[int(val) for val in input().split()]
print("given list=",lst)
print("maximum value from the given list= ",functools.reduce(lambda a,b:max(a,b),lst))
print("minmum value from the given lis=",functools.reduce(lambda a,b:min(a,b),lst))
