# Program for demonstrating Reading values by using  List Comprehension
print("Enter List of Values Separated by comma")
lst = [float(val) for val in input().split(",")]
print(lst, type(lst))

