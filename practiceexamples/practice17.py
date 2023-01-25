#program to generate and print a list except for the first 5 elements, where the values are square of numbers between 1 and 30 (both included)
def sqop():
    sqlist=[]
    for x in range(1,31):
        sqlist.append(x**2)
    print(sqlist[6:31])
sqop()

print("=======================================")

squarelist=[x**2 for x in range(1,31)]
print(squarelist[6:31])