#program for demonstrating variable length arguments
print("----------------------------------")
def sumnumbers(*args):
    total=0
    for number in args:
        total+=number
    return total
# call the function with multiple positional arguments
result=sumnumbers(1,2,3,4,5,6,7,8,9)
print(result)
# call the function with no positional arguments
result=sumnumbers()
print(result)
print("----------------------------------")

def key_v_l(**kwargs):
    for k,v in kwargs.items():
        print(k,"------>",v)
# call the function with multiple keyword arguments
key_v_l(name="vamsi",age="21",city="hyderabad")
# call the function with no keyword arguments
key_v_l()

print("---------------------------------")

def print_info(*name,**kwargs):
    print("name: ",name)
    for k , v in kwargs.items():
        print(k,"----------->",v)
print_info("vamsi","sai",age="21",designation="programmer")
print_info("sai","krishna")