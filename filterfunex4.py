#Filter the array, and return a new array with only the values equal to or above 18:
ages=[int(val) for val in input().split()]
#print(list(filter(lambda n: n>=18 , ages)))     #by using anonymous function
def fun(age):
    if(age<18):
        return False
    else:
        return True
result=filter(fun,ages)
res=list(result)
print(res)