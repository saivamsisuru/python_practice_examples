#program for Displaying Students marks report
while(True):
    sno=int(input("enter student number: "))
    sname=input("enter student name: ")
    while(True):
        cm=int(input("enter marks of c: "))
        if(cm>=0) and (cm<=100):
            break
        print("\t Enter valid marks")
    while(True):
        cppm=int(input("enter marks of c++: "))
        if(cppm>=0) and (cppm<=100):
            break
        print("\t Enter valid marks")
    while(True):
        pym=int(input("enter marks of python: "))
        if(pym>=0) and (pym<=100):
            break
        print("\t Enter valid marks")

    totmarks=cm+cppm+pym
    percent=(totmarks/300)*100

    if(cm<40) or (cppm<40) or (pym<40):
        grade="fail"
    else:
        if(totmarks<=300) and (totmarks>=250):
            grade="Distinction"
        if(totmarks<=249) and (totmarks>=200):
            grade="First"
        if(totmarks<=199) and (totmarks>=150):
            grade="Second"
        if(totmarks<=149) and (totmarks>=120):
            grade="Third"
    print("-"*50)
    print("\t S T U D E N T  M A R K S  R E P O R T")
    print("-"*50)
    print("\tstudent number :{}".format(sno))
    print("\tstudent name :{}".format(sname))
    print("\tstudent marks of c:{}".format(cm))
    print("\tstudent marks of c++:{}".format(cppm))
    print("\tstudent marks of python:{}".format(pym))
    print("="*50)
    print("\tTotal marks of student :{}".format(totmarks))
    print("\tPercentage of Student :{}".format(percent))
    print("\tgrade:{}".format(grade))
    print("-"*50)
    ch = input("Do u want to enter another student details(yes/no):")
    if (ch == "no"):
        print("Thx for using this program")
        break


