#program for operations of the atm
import sys
import Atmmenu
import Atmoperations as Atm


while(True):
    Atmmenu.menu()
    try:
        ch=int(input("Enter the choice: "))
        match(ch):
            case 1:
                Atm.Deposit()
            case 2:
                Atm.Withdraw()
            case 3:
                Atm.Bal()
            case 4:
                print("Thanks for using this ATM")
                sys.exit()
            case _:
                print("Enter correct input from the menu")
    except ValueError:
        print("Don't enter Alphanums,strs,symbols")

