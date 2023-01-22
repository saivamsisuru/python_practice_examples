#program for getting possitive and negative list from the given list by using list comprehension
lst=[2,3,0,-18,4,5,6,7,8,9,10]
posslist=[val for val in lst if(val>0)]
neglist=[val for val in lst if val<0 ]
print(posslist)
print(neglist)