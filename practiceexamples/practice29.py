#program to get unique values from a list
list=[val for val in input().split()]
print("given list=",list)
def remove_duplicates_list(list):
    combinedlst=[]
    duplicate_list=[]
    for i in list:
        if(i not in combinedlst):
            combinedlst.append(i)
        else:
            duplicate_list.append(i)

    return combinedlst , duplicate_list

res1,res2=remove_duplicates_list(list)

def unique_list(res1,res2):
    unique_list=[]
    for i in res1:
        if(i in res2):
            continue
        else:
            unique_list.append(i)
    print("unique values list from the given list=",unique_list)


unique_list(res1,res2)

