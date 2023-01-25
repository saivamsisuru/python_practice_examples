#program to find the second smallest number in a list
list = [int(x) for x in input().split()]
def second_smallest_number(list):
    list.sort()
    print(list)
    print("second smallest number in the list",list[1])
second_smallest_number(list)