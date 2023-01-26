def divisionop():
    print("Enter Two Values for Division:")
    a, b = float(input()), float(input())
    print("\tdiv({},{})={}".format(a, b, a / b))
    print("\tfloordiv({},{})={}".format(a,b,a//b))