#program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included). 
squared_num=[x**2 for x in range(1,31)]
y=squared_num[:5]
z=squared_num[-5:]
print("original list=",squared_num)
print("first 5 elements of their squares=",y)
print("last 5 elements of their squares=",z)

print("=========================================")
def squareop():
    sqlist=[]
    for x in range(1,31):
        sqlist.append(x**2)
    print(sqlist[:5])
    print(sqlist[-5:])
squareop()
