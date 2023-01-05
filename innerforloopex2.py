#program for generating multiplication table for list of given values
lst=[1,2,3,88,22,200,45]
for i in lst:
    if(i<1):
        continue
    else:
        print("="*50)
        for num in range(1,11):
            print("{} x {} ={}".format(i,num,num*i))
