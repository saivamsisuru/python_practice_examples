#program to shuffle and print a specified list
from random import shuffle
lst=[x for x in input().split()]
print("original list:",lst)
shuffle(lst)
print("shuffled list:",lst)