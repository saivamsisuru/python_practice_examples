#program for generating all sublists in the given list
list=[[1,2,3,3],[5,55,8],"s","e"]
counter=0
for i in list:
    if len(i)>1:
        counter+=1
        print(counter,i)