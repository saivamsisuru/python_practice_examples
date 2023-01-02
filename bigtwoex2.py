#program for accepting two  numerical values find the smallest among them and check for equality
a=int(input("enter value of a: "))
b=int(input("enter value of b: "))
res=a if a<b else b if b<a else "both values are equal"
print("smallest value of ({},{}) = {} ".format(a,b,res))
