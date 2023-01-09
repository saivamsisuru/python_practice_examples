#program for adding two numbers by using functions
def addop(a,b):
    c=a+b
    return c
a=float(input("Enter first value: "))
b=float(input("Enter second value: "))
c=addop(a,b)
print(c)
print(type(addop))
