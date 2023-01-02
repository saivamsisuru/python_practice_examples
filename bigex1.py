#program for accepting two  numerical values find the biggest among them anf check for equality
a=int(input("enter value of a: "))
b=int(input("enter value of b: "))
res=a if a>b else b if b>a else "Both values are equal"
print("big({},{})={}".format(a,b,res))
