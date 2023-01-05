#program for generating primes within the given range
n=int(input("enter lower value  "))
s=int(input("enter upper value "))
for num in range(n,s+1):
    if(num>1):
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
            print(num)
