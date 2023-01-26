#SharesDemo.py---A Program uses sharesInfo() of Shares Module--Viewing
import shares
import time,importlib
def  dispshares(d):
	print("-"*50)
	print("\tSharesName\tShareValue")
	print("-"*50)
	for sn,sv in d.items():
		print("\t{}\t\t{}".format(sn,sv))
	else:
		print("-"*50)


#main program
while(True):
    d=shares.sharesInfo()
    dispshares(d)
    print("Line-17 : I am Going to Sleep for 15 Seconds")
    time.sleep(15)
    print("Line-19: I am Coming Out-of Sleep ")
    importlib.reload(shares)
    ch=input("enter yes or no to continue: ")
    if(ch==yes):
        continue
    else:
        break

"""
d=shares.sharesInfo()
dispshares(d)
print("Line-23 : I am Going to Sleep for 15 Seconds")
time.sleep(15)
print("Line-25: I am Coming Out-of Sleep ")
importlib.reload(shares)
d=shares.sharesInfo()
dispshares(d)
"""