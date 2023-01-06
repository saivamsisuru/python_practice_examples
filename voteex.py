#program for accepting age of citizen and decide whether the citizen is eligible to vote or not
while(True):
    n=int(input("enter the age: "))
    if(n>=18):
        print("eligible to vote")
        break
    else:
        print("not eligible to vote")
        print("Try again")
