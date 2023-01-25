#program to append a list to the second list

# append one list to another using the extend()
print("====== append one list to another using the extend()==========")
lst1=[x for x in input().split()]
lst2=[x for x in input().split()]
print("original first list",lst1)
print("original second list",lst2)
lst2.extend(lst1)
print(lst2)
print("="*50)
# append one list to another using the += operator
print("====== append one list to another using the += operator==========")
lst1=[x for x in input().split()]
lst2=[x for x in input().split()]
print("original first list",lst1)
print("original second list",lst2)
lst2=lst2+lst1
print(lst2)
print("="*50)
# append one list to another using the + operator
print("====== append one list to another using the + operator==========")
lst1=[x for x in input().split()]
lst2=[x for x in input().split()]
print("original first list",lst1)
print("original second list",lst2)
lst2=lst2+lst1
print(lst2)
print("="*50)