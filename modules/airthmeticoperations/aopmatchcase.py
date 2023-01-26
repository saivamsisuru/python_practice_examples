import sys
import menu
from add import addop 
from sub import subop
from mul import mulop
from division import divisionop
from modulodiv import modulodivop
from exponential import exponentialop
from sqrt import sqrtop
while(True):
    menu.Menu()
    ch=int(input("Enter Ur Choice: "))
    print("	=============================")
    match(ch):
        case (1):
            addop()
        case (2):
            subop()
        case (3):
            mulop()
        case (4):
            divisionop()
        case (5):
            modulodivop()
        case (6):
            exponentialop()
        case (7):
            sqrtop()
        case (8):
            print("thanks for using this program")
            break #sys.exit()
        case (_):
            print("your selection of values are wrong please try again")
print("program execution is completed")


