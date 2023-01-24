#program to print the numbers of a specified list after removing even numbers from it
lst=[int(val) for val in input().split()]
nl=[x for x in lst if x%2!=0]
print(nl)