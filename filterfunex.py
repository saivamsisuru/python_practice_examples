#program for accepting list for values which will obtain list of even numbers and odd numbers
lst=[int(val) for val in input().split()]
evenlist=list(filter(lambda n: n%2==0 ,lst))
oddlist=list(filter(lambda n:n%2!=0,lst))
print(evenlist)
print(oddlist)
