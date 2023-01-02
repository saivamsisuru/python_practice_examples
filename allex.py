#program to check whether the given word is vowel or consonent or numeric or Alphanumeric or special symbol
word=input("enter a word ")
x=word.isnumeric()
y=word.isalnum()
z=word.isalpha()
res="this is a vowel word" if 'a' in word.lower() or 'e' in word.lower() or 'i' in word.lower() or 'o' in word.lower() or 'u' in word.lower() else "this is consonent word"  if z is True else "this is numeric" if x is True else "this is alphanumeric" if y is True else "this is special symbol"
print("'{}' {}".format(word,res))