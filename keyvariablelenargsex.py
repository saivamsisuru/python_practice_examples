#program for demonstrating key word variable length arguments
print("-------------------------------------")
def my_func(reqarg,optarg=10,**kwargs):
    print(reqarg)
    print(optarg)
    print(kwargs)
my_func("sai",20,name="vamsi",age="21")

print("--------------------------------------")

def my_function(reqarg,**kwargs):
    result=reqarg
    for k , v in kwargs.items():
        if k == "add":
            result+=v
        elif k=="sub":
            result-=v
        elif k=="mul":
            result*=v
    return result
result=my_function(reqarg=10,add=5,mul=20)
print(result)
print("==================")

def fun(reqarg,**kwargs):
    result=reqarg
    for k,v in kwargs.items():
        if k=='concate':
            result+=v
        elif k=='replace':
            result = v
    return result
print(fun(reqarg="HELLO",concate="WORLD"))

