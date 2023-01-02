#program for accepting three numerical values find the smallest among them and check for equality
a=int(input("enter value of a: "))
b=int(input("enter value of b: "))
c=int(input("enter value of c: "))
res=a if a<=b and a<c else b if b<a and b<=c else c if c<=a and c<b else "all the values are equal"
print("biggest values of ({},{},{})={}".format(a,b,c,res))
