#program for writing the file
try:
    fp=open("first.data","w")
    print(type(fp))
    print("----------------------------------------------------------")
    print("Name of the file=",fp.name)
    print("File Opening Mode:", fp.mode)
    print("If File Readable?:",fp.readable())
    print("If File Writeable?:",fp.writable())
    print("Line-12: is File Closed:",fp.closed) 
    print("----------------------------------------------------------")
except :
    print("something went wrong")
finally:
    print("I am from finally Block")
    fp.close() # manual Closing by using close()
    print("Line:18: is File Closed:",fp.closed) 
print("================================================")
try:
    with open("first.data","w") as fp:
        print(type(fp))
        print("Name of the file: ",fp.name)
        print("File opening Mode: ",fp.mode)
        print("If file Readable?:",fp.readable())
        print("If file writeable?:",fp.writable())
        print("Line-12: is file closed:",fp.closed)
except :
    print("something went wrong")
finally:
    print("Iam from finally block")
    fp.close()
    print("Line:32 is file closed:",fp.closed)