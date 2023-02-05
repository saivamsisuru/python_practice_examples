#program for open the file in "a+" mode 
with open("emp.data","a+") as fp:
    print("======================")
    print("Name of the file=",fp.name)
    print("File Opening Mode:", fp.mode)
    print("If File Readable?:",fp.readable())
    print("If File Writeable?:",fp.writable())
    print("Line-9: is File Closed:",fp.closed)
    print("======================")
    
print("Line-11: is File Closed:",fp.closed)

    
