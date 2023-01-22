#program for getting even and odd list from the given list by using list comprehension
lst=[2,3,0,-18,4,5,6,7,8,9,10]
evenlist=[val for val in lst if(val>0) and val%2==0]
oddlist=[val for val in lst if val>0 and val%2!=0 ]
print(evenlist)
print(oddlist)