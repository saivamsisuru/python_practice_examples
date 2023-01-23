#program for accepting a line of text and filter for vowels
lst=[val for val in input()]
print("\t vowels are ")
print(list(filter(lambda ch: ch.lower() in ["a","e","i","o","u"],lst)))


