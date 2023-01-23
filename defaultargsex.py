#program for demonstrating defaut arguments
print("---------------------------------------------------")
def add(num1,num2=0):
    return num1+num2
result=add(5,6)
print(result)
result=add(6)
print(result)

print("---------------------------------------------------")

def divide(divident,divisor=2):
    return divident/divisor
result=divide(20,5)
print(result)
result=divide(20)
print(result)

print("----------------------------------------------------")

def mul(number,factor=1):
    lst=[x*factor for x in number]
    return lst
result=mul([5,4,6],2)
print(result)
result=mul([2,8,9])
print(result)
print("--------------------------------------------------------")
