#program for generating password
import random
upper_case="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case="abcdefghijklmnopqrstuvwxyz"
number="0123456789"
symbol="!~@#$%^&*()_+*\|{};""-=',./?`"
x=upper_case+lower_case+number+symbol
length_of_password=8
password="".join(random.sample(x,length_of_password))
print(password)