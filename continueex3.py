#program for displaying list of +ve values and -ve from a given list of values
lst=[10,-45,-11,155645,35,58,-4,3128,-78,-5,-7,5,5,6,5458,55,-7,]
print("+ve values from the list")
for i in lst:
    if(i<=0):
        continue
    print(i)
print("-"*50)
print(" -ve values from the list")
for i in lst:
    if(i>=0):
        continue
    print(i)