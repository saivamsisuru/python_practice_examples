import sys
print("=============================")
print("\t	Arithmetic Operations")
print("	=============================")
print("\t	1. Addition")
print("\t	2. Substraction")
print("\t	3. Multiplication")
print("\t	4. Division")
print("\t	5. Modulo Division")
print("\t	6. Exponentiation")
print("\t	7. Exit")
print("	=============================")
ch=int(input("	Enter Ur Choice: "))
print("	=============================")
match(ch):
    case 1:
        print("Enter Two Values for Addition:")
        a, b = float(input()), float(input())
        print("\tsum({},{})={}".format(a, b, a + b))
    case 2:
        print("Enter Two Values for substraction:")
        a, b = float(input()), float(input())
        print("\tsub({},{})={}".format(a, b, a - b))
    case 3:
        print("Enter Two Values for multiplication:")
        a, b = float(input()), float(input())
        print("\tmul({},{})={}".format(a, b, a * b))
    case 4:
        print("Enter Two Values for Division:")
        a, b = float(input()), float(input())
        print("\tdiv({},{})={}".format(a, b, a / b))
        print("\tfloordiv({},{})={}".format(a,b,a//b))
    case 5:
        print("Enter Two Values for MOd Div:")
        a, b = float(input()), float(input())
        print("\tmod({},{})={}".format(a, b, a % b))
    case 6:
        print("enter two values for exponentiation:")
        a, b=float(input()), float(input())
        print("\texp({},{})={}".format(a,b,a**b))
    case 7:
        print("thanks for using this program")
        sys.exit()
    case _:
        print("your selection of values are wrong please try again")
print("program execution is completed")


