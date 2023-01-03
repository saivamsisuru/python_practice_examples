#program for accepting any word or sensitive and print no of  occurences of each letter
s=input("enter any word or sentence: ")
d={}
for i in s:
    if(i not in d):
        d[i]=1
    else:
        d[i]=d.get(i)+1
else:
    print(d)
