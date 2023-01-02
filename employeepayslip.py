#Program for generating pay slip of an employee
eno=int(input("enter employee number: "))
ename=input("enter employee name: ")
ebasicsal=float(input("enter employee basic salary: "))
if (ebasicsal==0):
    print("{} Invalid Salary--Read Python Notes!!!".format(ebasicsal))
else:
    if (ebasicsal>=10000):
        da=ebasicsal*(20/100)
        ta=ebasicsal*(15/100)
        hra=ebasicsal*(10/100)
        ma=ebasicsal*(2/100)
        lic=ebasicsal*(2/100)
        gpf=ebasicsal*(1.5/100)
    else:
        da = round(ebasicsal * (10 / 100), 2)
        ta = round(ebasicsal * (8 / 100), 2)
        hra = round(ebasicsal * (6 / 100), 2)
        ma = round(ebasicsal * (3 / 100), 2)
        lic = round(ebasicsal * (1 / 100), 2)
        gpf = round(ebasicsal * (1.5 / 100), 2)
        netsal=(ebasicsal+da+ta+hra+ma)-(lic+gpf)
        print("=" * 50)
        print("displaying the pay slip of an employee")
        # display the pay slip
        print("=" * 60)
        print("\tEmployee Pay Slip")
        print("=" * 60)
        print("\tEmployee Number:{}".format(eno))
        print("\tEmployee Name:{}".format(ename))
        print("\tEmployee Basic Salary:{}".format(ebasicsal))
        print("\tEmployee DA:{}".format(da))
        print("\tEmployee TA:{}".format(ta))
        print("\tEmployee HRA:{}".format(hra))
        print("\tEmployee MA:{}".format(ma))
        print("Deductions:")
        print("\tEmployee LIC:{}".format(lic))
        print("\tEmployee GPF:{}".format(gpf))
        print("-" * 50)
        print("\tEmployee Net Salary:{}".format(netsal))
        print("=" * 50)


