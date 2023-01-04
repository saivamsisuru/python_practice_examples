#program for demonstrating continue statement in for loop
s='PYTHON'
for i in s:
    if(i=="H") or (i=="O"):
        continue
    print(i)
else:
    print("for else continue statement")#Here else block will be executes in continue statement 
print("other statements")