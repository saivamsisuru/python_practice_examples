#program for demonstrating continue statement in while loop
s='PYTHON'
i=0
while(i<len(s)):
    if(s[i]=="H") or (s[i]=="O"):
        i=i+1
        continue
    print(s[i])
    i=i+1
else:
    print("for else continue statement")#Here else block will be executes in continue statement
print("other statements")