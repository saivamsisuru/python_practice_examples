#program for demonstrating break statement in while loop
s="PYTHON"
i=0
while (i<len(s)):
    if(s[i]=="H"):
        break
    else:
        print(s[i])
        i = i + 1
else:
    print("for else break statement")#while using break in while loop else block of that while loop will not execute
print("other statements in program")
