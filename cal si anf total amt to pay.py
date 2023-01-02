#calculate simple interest and total amt to pay
p=float(input("enter principle amount: "))
t=float(input("enter time period: "))
r=int(input("enter rate of interest: "))
si=(p*t*r)/100
totamt=si+p
print(" principle amount {}".format(p))
print(" time period {}".format(t))
print(" rate of interest {}".format(r))
print("simple interest {}".format(si))
print("total amount {}".format(totamt))