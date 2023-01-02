#program which will accept three numerical integer values and find biggest among them and check for equality by using simple if statement
a=int(input("enter the value of a: "))
b=int(input("enter the value of b: "))
c=int(input("enter the value of c: "))
if (b<a>=c):
    print("big of {},{},{} is {}".format(a, b, c, a))
if (a<=b>c):
    print("big of {},{},{} is {}".format(a, b, c, b))
if (a<c>=b):
    print("big of {},{},{} is {}".format(a, b, c, c))
if (b>a<=c):
    print("smaller of {},{},{} is {}".format(a, b, c, a))
if (a>=b<c):
    print("smaller of {},{},{} is {}".format(a, b, c, b))
if (a>c<=b):
    print("smaller of {},{},{} is {}".format(a, b, c, c))
if (a==b==c):
    print("All values are equal")
print("Program is executed successfully")