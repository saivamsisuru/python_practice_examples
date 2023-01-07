#program for accepting list of values from the keyboard until we press stop
lst = []
while(True):
    n=input("enter any value: ")
    if (n == "stop"):
        break
    else:
        lst.append(n)
print(lst)




