#program for accepting list of words and filter those words whose first letter and last letter is same
lst=[val for val in input().split(",")]
print(list(filter(lambda lst: lst[0]==lst[-1],lst)))
