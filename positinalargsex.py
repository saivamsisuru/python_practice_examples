#program for demonstrating positional arguments

print("------------------------------------------------------")

def sumop(a,b):
    return a+b
sum=sumop(2,5)
print(sum)

print("------------------------------------------------------")

def mul(*args):
    product=1
    for i in args:
        product *= i
    return product
result = mul(2,3,4)
print(result)

print("------------------------------------------------------")

def divide(divident,divisor=2):
    return divident / divisor
result=divide(10,5)
print(result)
result=divide(10)
print(result)

print("------------------------------------------------------")

