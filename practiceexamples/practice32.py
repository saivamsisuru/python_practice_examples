#program to check whether a list contains a sublist
def is_sublist(lst):
    for i in lst:
        if len(i)>1:
            print("sublist is present in list")
            break
        else:
            print("sublist is not present in list")
    
lst=[[1258,1,5,447,5],"s",["shs","dhhd","fhh"]]
is_sublist(lst)

