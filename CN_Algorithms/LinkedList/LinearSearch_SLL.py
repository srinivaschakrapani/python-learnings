class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def linearSearchRecursive(head, n):
    #  Given a linked list and an integer n you need to find and return index
    #  where n is present in the LL. Do this iteratively. Return -1 if n is not
    #  present in the LL. Indexing of nodes starts from 0.
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if head is None:
        return -1
    elif n == head.data:
        return 0
    else:
        small_output = linearSearchRecursive(head.next, n)
        if small_output == -1:
            return -1
        else:
            return 1 + small_output
def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
data=int(input())
index = linearSearchRecursive(l, data)
print(index)
'''
3 4 5 2 6 1 9 -1
8
'''