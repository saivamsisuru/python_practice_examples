#program to access the index of a list
lst=[1,2,3,4,5,'banana','apple',9]
#Get all the indexes in the list
for val in lst:
    index=lst.index(val)
    print(index , val)
    
print("==================")
#Get the index of an element in the list using enumerate function
print(lst.index('banana'))

print("==================")
#Get the index of an element in the list using enumerate function
for ind, value in enumerate(lst):
    if value == 'banana' :
        print(ind,value)

