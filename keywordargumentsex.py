#program for demonstrating keyword arguments
def print_info(name,age):
    print("Name: ",name)
    print("Age: ",age)
name=input("enter name")
age=int(input("enter your age"))
print_info(name,age)

print("-----------------------------------------------")
def print_keyword_args(**kwargs):   #arbitary no of values
    for k,v in kwargs.items():
        print(k  ,":",  v)

print_keyword_args(name="vasu",age=21,city="hyderabad",state="TS")

print("-----------------------------------------------")

def divide(divident,divisor=2):
    return divident/divisor
result=divide(divident=10,divisor=5)   #function calling with positional argument and keyword argument
print(result)
result=divide(divident=10)    #function calling omly with positional argument
print(result)

print("-----------------------------------------------")

def my_function(reqkwordarg,optargument=10,**kwargs):
    print(reqkwordarg)
    print(optargument)
    print(kwargs)
my_function(reqkwordarg="vamsi",optargument=25,area="sr nagar",city="hyderabad",pin=500038)