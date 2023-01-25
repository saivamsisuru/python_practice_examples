#program to find the second largest number in a list
list = [int(x) for x in input().split()]
def second_largest_number(list):
    list.sort(reverse=True)
    print(list)
    print("second largest number in the list",list[1])
second_largest_number(list)