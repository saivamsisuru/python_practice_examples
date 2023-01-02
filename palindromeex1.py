#program which will accept a word from keyboard and decide whether it is a palindrome
word=input("enter a word: ")
x=word==word[::-1]
val="palindrome" if x else "is not palindrome"
print("given {} is {}".format(word,val))