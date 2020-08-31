class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_Iterative_v4(head):
    if head is None:
        return head
    else:
        prev = None
        curr = head
        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
# What if I dont want to return tail
# where is tail ? its is present at head.next
def reverseRecursive_v3(head):
    if head.next is None:
        return head
    small_head = reverseRecursive_v3(head.next)
    tail = head.next
    tail.next = head
    head.next = None
    return small_head


# Return the tail node from the recursion and point the tail to head
def reverseRecursive_v2(head):
    if head.next is None:
        return head, head
    else:
        small_head, small_tail = reverseRecursive_v2(head.next)
        small_tail.next = head
        head.next = None
        return small_head, head


def reverseRecursive(head, newhead):
    if head is None:
        return newhead
    else:
        nxt = head.next
        head.next = newhead
        newhead = head
        head = nxt
        return reverseRecursive(head, newhead)
    #  Given a linked list, reverse it recursively.
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################


#     if head is None or head.next is None:
#         return head

#     small_head = reverseRecursive(head.next)
#     tail = small_head
#     while tail.next is not None:
#         tail = tail.next
#     tail.next = head
#     head.next = None
#     return small_head

def ll(arr):
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head


def printll(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()


# Main
from sys import setrecursionlimit

setrecursionlimit(11000)
# Read the link list elements including -1
arr = list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
# l = reverseRecursive(l, None)
#head, tail = reverseRecursive_v2(l)
#printll(l)
#l = head
#l = reverseRecursive_v3(l)
l = reverse_Iterative_v4(l)
printll(l)
