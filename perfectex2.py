#program for accepting any numerical positive number and decide whether the given number is perfect or not
n=int(input("enter lower value: "))
s=int(input("enter upper value: "))
pfnumlist=[]
npfnumlist=[]
for num in range(n,s):
    if(num>=1):
        fs=0
        #print("~"*50)
        for i in range(1,(num//2)+1):
            if(num%i==0):
                #print("\t factors of {} are {}".format(num,i))
                fs=fs+i
        else:
            #print("-" * 50)
            #print("\tsum of factors of {} are {}".format(num,fs))
            if (fs == num):
                #print("-" * 50)
                #print("\t{} is PERFECT".format(num))
                #print("$" * 50)
                pfnumlist.append(num)
            else:
                #print("-" * 50)
                #print("\t{} is not a PERFECT".format(num))
                #print("$" * 50)
                npfnumlist.append(num)
else:
    print("\t List of perfect numbers from {} to {} are {}".format(n,s,pfnumlist))

