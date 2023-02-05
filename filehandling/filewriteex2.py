#program for appending mode
try:
    fp=open("first1.data","a")
    print("======================")
    print("Name of the file=",fp.name)
    print("File Opening Mode:", fp.mode)
    print("If File Readable?:",fp.readable())
    print("If File Writeable?:",fp.writable())
    print("Line-9: is File Closed:",fp.closed)
    print("======================")
#except FileExistsError:
 #   print("file exists already")
    
finally:
    print("it is finally block")
    fp.close()
    print("line-16 is file closed:",fp.closed)
