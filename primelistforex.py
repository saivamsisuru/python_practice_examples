#program for displaying prime numbers in a given list of numbers
lst=[0,1,2,3,4,5,6,7,8,9,10,11,12]
primelist,nplist=[],[]
for num in lst:
    if(num<=1):
        continue
    else:
        res=True
        for i in range(2,num):
            if(num%i==0):
                res=False
                break
        if (res):
            primelist.append(num)
        else:
            nplist.append(num)
else:
    print("list of given values are {}".format(lst))
    print("list of primes from the given list {}".format(primelist))
    print("list of not primes from the given list {}".format(nplist))