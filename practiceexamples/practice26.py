# program to check whether two lists are circularly identical
"""
Circularly identical means that two or more items are identical, but in a circular fashion. 
This means that if the items are represented as a sequence, the last item of the sequence is the same as the first item of the sequence.

For example, if we have two lists, list1 = [1, 2, 3] and list2 = [3, 1, 2], they are circularly identical because the
last item of list1 is the same as the first item of list2, and vice versa.

Another example, if we have two strings, str1 = "abc" and str2 = "cab", they are also circularly identical because the 
last letter of str1 is the same as the first letter of str2, and vice versa.

Circular identity is often used in mathematical, computer science and computational biology contexts,
 such as in the study of permutations, and in DNA sequencing where circularly identical sequences of genetic material 
 can indicate a circular chromosome.

It's worth noting that if two items are circularly identical, it doesn't mean that the items are the same. 
The items must be identical in order for them to be considered circularly identical.

"""

def circularly_identical(list1,list2):
    # Check if the lists have the same length
    if (len(list1) != len(list2)):
        return False
    # Check if the lists are identical in any order
    if (set(list1) != set(list2)):
        return False
    # Check if the lists are circularly identical
    for i in range(len(list1)):
        if(list1[i:]+list1[:i]==list2):
            return True
    return False

list1 = [x for x in input().split()]
list2 = [x for x in input().split()]
print(circularly_identical(list1,list2))
