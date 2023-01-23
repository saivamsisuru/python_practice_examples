#program for accepting list of values and obtain their square
lst=[int(val) for val in input().split()]
print(list(map(lambda n:n**2,lst)))