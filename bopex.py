# swapping of two numerical values by using bitwise xor operator
a = int(input("enter value of a: "))
b = int(input("enter value of b: "))
print("=" * 150)
# printing original values
print("original value of a: {}".format(a))
print("original value of b: {}".format(b))
print("=" * 150)
# swapping method 
# t=a
# a=b
# b=t
# a,b=b,a
a = a ^ b
b = a ^ b
a = a ^ b
print("swapped value of a: {}".format(a))
print("swapped value of b: {}".format(b))
print("=" * 150)
