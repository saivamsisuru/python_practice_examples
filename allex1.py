#program for checking the given value or word is numeric or alphanumeric or special symbol
word=input("enter a value")
x=word.isnumeric()
y=word.isalnum()
res="this is numeric" if x is True else "alphanumeric" if y is True else "special symbol"
print(res)
