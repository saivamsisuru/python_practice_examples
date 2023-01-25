#program to generate all permutations of a list in Python.
import itertools
lst=[int(val) for val in input().split()]
print(list(itertools.permutations(lst)))
print(list(itertools.permutations(lst,2)))  # with length of the permutation