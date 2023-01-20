#program for accepting any three numerical values and find the biggest and smallest among them by using anonymous functions

big=lambda a,b,c: a if a>=b and a>c else b if b>a and b>=c else c if c>=a and c>b else "all are equal"
small=lambda a,b,c: a if a<=b and a<c else b if b<a and b<=c else c if c<=a and c<b else "all are equal"

#main program
a=int(input("enter value of a: "))
b=int(input("enter value of b: "))
c=int(input("enter value of c: "))
res1=big(a,b,c)
res2=small(a,b,c)
print("\t{} is bigger among the {},{},{}".format(res1,a,b,c))
print("\t{} is smaller among the {},{},{}".format(res2,a,b,c))