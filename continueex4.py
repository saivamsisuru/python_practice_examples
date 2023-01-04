#program for displaying list of +ve values and -ve values in a separate lists from a given list of values
lst=[10,-45,-11,155645,35,58,-4,3128,-78,-5,-7,5,5,6,5458,55,-7,0]
pslst,nglst=[],[]
for i in lst:
    if(i<=0):
        continue
    pslst.append(i)
print("-"*50)
for i in lst:
    if(i>=0):
        continue
    nglst.append(i)
print("List of +ve values{} from the list {} ".format(pslst,lst))
print("List of -ve values{} from the list {} ".format(nglst,lst))

