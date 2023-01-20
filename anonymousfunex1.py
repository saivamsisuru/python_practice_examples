#program for accepting any two numerical values and find the biggest among them by using anonymous functions

findbig=lambda a,b: a if a>b else b if b>a else "Both Values are equal"

#main program
a=int(input("Enter Value of a:"))
b=int(input("Enter Value of b:"))
res=findbig(a,b)
print("big({},{})={}".format(a,b,res))