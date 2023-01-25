#program that demonstrates how to append a list to another list and retain the original list's format


# append one list to another using the extend()
print("====== append one list to another using the extend()==========")
lst1=[x for x in input().split()]
lst2=[x for x in input().split()]
print("original first list",lst1)
print("original second list",lst2)
lst2.extend([lst1])
print("appended list",lst2)
print("="*50)
# append one list to another using the += operator
print("====== append one list to another using the += operator==========")
lst1=[x for x in input().split()]
lst2=[x for x in input().split()]
print("original first list",lst1)
print("original second list",lst2)
lst2=lst2+[lst1]
print("appended list",lst2)
print("="*50)
# append one list to another using the + operator
print("====== append one list to another using the + operator==========")
lst1=[x for x in input().split()]
lst2=[x for x in input().split()]
print("original first list",lst1)
print("original second list",lst2)
lst2=lst2+[lst1]
print("appended list",lst2)
print("="*50)