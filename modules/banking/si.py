def simpleint():
    p=int(input("enter principal amount: "))
    t=int(input("enter time: "))
    r=float(input("enter rate of interest: "))
    si=(p*t*r)/100
    print(si)