#program for demonstrating reduce function
import functools
print("========by using normal function===============")
def sumop(a,b):
    return a+b
x=functools.reduce(sumop,[int(val) for val in input().split()])
print(x)

print("========by using anonymous function===============")
print(functools.reduce(lambda a,b:a+b ,[int(val) for val in input().split()]))

