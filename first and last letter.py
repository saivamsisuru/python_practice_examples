#program which will obtain the word those first letter and last letter is same
x=input("enter given word: ")
val=x[0]==x[-1]
val=x[0]==x[len(x)-1]
res="first and last values are same" if val is True else "first and last values are different"
print(" '{}' has {}".format(x,res))