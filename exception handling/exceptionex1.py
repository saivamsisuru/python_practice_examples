try:
    a=input("enter first value: ")
    b=input("enter second value: ")
    x=int(a)
    y=int(b)
    z=x/y
    
except ZeroDivisionError:
    print("dont enter zero in the denominator")
except ValueError:
    print("Dont enter alpha numeric , symbols ")
else:
    print(z)
finally:
    print("program is executed successfully")
