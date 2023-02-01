#program to find common items from two lists.
print("===========using intersection between sets===============")
l1=[5,46,5,6,5,5]
l2=[2,6,5,6,5,6]
l3=set(l1).intersection(l2)
print(l3)
print("=========using membership operator=========")
l1=[5,46,5,6,5,5]
l2=[2,6,5,6,5,6]
print([i for i in l1 if i in l2])
print("=======using & operator between two sets=========")
l1=[5,46,5,6,5,5]
l2=[2,6,5,6,5,6]
print(set(l1) & set(l2))
print("=====using collections module========")
import collections
l1=[5,46,5,6,5,5]
l2=[2,6,5,6,5,6]
print(collections.Counter(l1)&collections.Counter(l2))
print("======using operator module==========")
import operator as op
l1=[5,46,5,6,5,5]
l2=[2,6,5,6,5,6]
print([i for i in l1 if op.countOf(l2,i)>0])
print("==================")