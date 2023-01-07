#program for converting the temperature in celsius to fahrenheit and kelvin where celsius temp must be +ve
while(True):
    celsiustemp=float(input("enter the temperature:"))
    if(celsiustemp<0):
        print("invalid input")
    else:
        fahrenheit=(celsiustemp*1.8)+32
        kelvin=celsiustemp+273.15
        print("\t{} degreecelsius in fahrenheit {}F".format(celsiustemp,fahrenheit))
        print("\t{} degreecelsius in Kelvin {}K".format(celsiustemp,kelvin))
        ch=input("enter yes/no to continue or not: ")
        if(ch=="no"):
            print("thanks for using the program")
            break
        else:
            continue

