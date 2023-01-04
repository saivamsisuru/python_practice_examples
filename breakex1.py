#program for demonstrating break statement in for loop
s="PYTHON"
for i in s:
    if(i=="H"):
        break
    else:
        print(i)
else:
    print("for else break statement")#while using break in for loop else block of that for loop will not execute
print("other statements in program")
