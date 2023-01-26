from menu import Menu as m
import rect as r
import square as s
import circle as c
import sys
while(True):
    m()
    ch=int(input("enter a number listed below to access the menu: "))
    match(ch):
        case(1):
            r.area()
            print("="*40)
        case(2):
            s.area()
            print("="*40)
        case(3):
            c.area()
            print("="*40)
        case(4):
            print("Thanks for using this program")
            print("="*40)
            sys.exit()
        case(_):
            print("You enter invalid input pls try again-choose correct input from the menu")

