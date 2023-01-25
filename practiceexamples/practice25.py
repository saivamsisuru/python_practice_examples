#program to select an item randomly from a list.
import random
#by using random.sample()
print("===========by using random.sample()===========")
lst=[x for x in input().split()]
print(random.sample(lst,k=1)[0])
#by using random.choice()
print("==========by using random.choice()=============")
lst=[x for x in input().split()]
print(random.choice(lst))
#by using random.randint()
print("========by using random.randint()==========")
lst=[int(x) for x in input().split()]
print(random.randint(0,len(lst)-1))
