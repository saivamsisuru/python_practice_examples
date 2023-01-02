#program for accepting three numeric values and find the smallest among them and check for equality by using if..else statement
a=int(input("enter the value of a: "))
b=int(input("enter the value of b: "))
c=int(input("enter the value of c: "))
if(a<b) and (a<=c):  # Logic for small---a
    print("small({},{},{})={}".format(a,b,c,a))
else:
    if(b<=a) and (b<c):# Logic for small---b
        print("small({},{},{})={}".format(a, b, c, b))
    else:
        if(c<a) and (c<=b):  # Logic for small---c
            print("small({},{},{})={}".format(a, b, c, c))
        else:
            print("ALL VALUES ARE EQUAL")
print("Program execution completed")