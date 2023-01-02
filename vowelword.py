#program which will accept a word and check whether it contains vowels or not 
word=input("enter the word: ")
res="is vowel word " if 'a' in word.lower() or 'e' in word.lower() or 'i' in word.lower() or 'o' in word.lower() or 'u' in word.lower() else "is not vowel word"
print("{} {}".format(word,res))
