#program for accepting list of values and obtain their square
lst=[int(val) for val in input().split()]
print(list(map(lambda n:n**2,lst)))


print("===========================================")

#Calculate the length of each word in the tuple:
tpl=(val for val in input().split())
length=(tuple(map(lambda wrd: len(wrd),tpl)))
print(length)
fs=0
for i in length:
    fs+=i
print(fs)

print("===========================================")

#Make new fruits by sending two iterable objects into the function:
def funtion(a,b):
    return a+b
print(list(map(funtion,("water","jack"),("melon","fruit"))))