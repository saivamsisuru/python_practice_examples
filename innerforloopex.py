#Program for demonstrating for in for
n=int(input("enter any number"))
for i in range(1,n):
    print(i)
    for j in range(1,4):
        print("\t {}".format(j))