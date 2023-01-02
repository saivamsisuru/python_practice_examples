#swapping of two values
a=input("enter value of a: ")
b=input("enter value of b: ")
print("="*150)
#printing original values
print("original value of a: {}".format(a))
print("original value of b: {}".format(b))
print("="*150)
#swapping method
#t=a
#a=b
#b=t
a,b=b,a
print("swapped value of a: {}".format(a))
print("swapped value of b: {}".format(b))
print("="*150)
