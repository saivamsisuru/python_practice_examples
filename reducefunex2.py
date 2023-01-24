#program for demonstrating reduce function (concatinating strings in a given list)
import functools
print("========by using join function==========")
lst=[val for val in input().split()]
res=" ".join(lst)
print(res)

print("=========by using reduce function===========")
print(functools.reduce(lambda a,b:a+" "+b,[val for val in input().split()]))


