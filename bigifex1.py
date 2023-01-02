#program for accepting two numerical int values and find the biggest and smaller among them and check for the equality by using simple if
a=int(input("enter the value of a: "))
b=int(input("enter the value of b: "))
if (a>b):
    print("{} is bigger than {}".format(a,b))
if (b>a):
    print("{} is bigger than {}".format(b,a))
if (a<b):
    print("{} is smaller than {}".format(a,b))
if (b<a):
    print("{} is smaller than {}".format(b,a))
if (a==b):
    print("Both values are equal")
print("execution of program is finished ")