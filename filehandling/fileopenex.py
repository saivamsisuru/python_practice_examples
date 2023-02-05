#program for reading the file 
try:
    fp=open("first.data")
    print("Type of fp=",type(fp))
    print("File Opened Sucessfully in read mode:")
    print("----------------------------------------------------------")
    print("Name of the file=",fp.name)
    print("File Opening Mode:", fp.mode)
    print("If File Readable?:",fp.readable())
    print("If File Wrieable?:",fp.writable())
    print("Line-12: is File Closed:",fp.closed) 
    print("----------------------------------------------------------")
except FileNotFoundError:
    print("File is not located,please create a file")
finally:
    print("I am from finally Block")
    fp.close() # manual Closing by using close()
    print("Line:18: is File Closed:",fp.closed) 