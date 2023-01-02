import sys
print("=============================")
print("\t	Arithmetic Operations")
print("	=============================")
print("\t	R. Rectangle")
print("\t	S. Square")
print("\t	T. Triangle")
print("\t	C. Circle")
print("\t	E. Exit")
print("	=============================")
ch=input("	Enter Ur Choice: ")
print("	=============================")
match(ch.upper()):
    case "R":
        print("Enter values of length and breadth")
        l,b=float(input()),float(input())
        print("Area of rectangle ({},{})={}".format(l,b,l*b))
    case 'S':
        print("Enter value of side")
        a=float(input())
        print("area of side {}={}".format(a,a*a))
    case 'T':
        print("enter values of Base and Height")
        b,h=float(input("enter base: ")),float(input("enter height:"))
        print("area of triangle ({},{})={}".format(b,h,1/2*b*h))
    case 'C':
        print("enter value of radius")
        r=float(input("enter radius value"))
        print("area of circle for given radius {} = {}".format(r,3.14*(r**2)))
    case 'E':
        print("thanks for using program")
        sys.exit()
    case _:
        print("entered value is wrong try again")