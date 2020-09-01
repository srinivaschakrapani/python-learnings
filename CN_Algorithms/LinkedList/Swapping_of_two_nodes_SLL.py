# Still in progress

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def swapTwoNodes(head, M, N):
    #  Given a linked list and two integers M and N. Traverse the linked list
    #  such that you retain M nodes then delete next N nodes, continue the same
    #  until end of the linked list. That is, in the given linked list you need
    #  to delete N nodes after every M nodes.
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if M == N:
        return head
    if head is None or head.next is None:
        return head
    if M > N:
        M,N = N,M
    prev1 = None
    curr1 = None
    prev2 = None
    curr2 = None
    prev = None
    curr = head
    i = j = 0
    while curr is not None:
        if i == M:
            prev1 = prev
            curr1 = curr
        if j == N:
            prev2 = prev
            curr2 = curr
        i += 1
        j += 1
        prev = curr
        curr = curr.next
    # If one of the nodes to be swapped is head
    if prev1 is None:
        prev2.next = curr1
        tmp = curr1.next
        curr1.next = curr2.next
        curr2.next = tmp
        head = curr2
    # elif prev1 == None and abs(M-N) == 1:
    #     curr1.next = curr2
    #     curr2.next = curr1
    #     head = curr2
    #for adjacent nodes
    elif abs(M-N) == 1:
        prev1.next = curr2
        curr1.next = curr2.next
        curr2.next = curr1
    else:
        prev1.next = curr2
        tmp = curr1.next
        curr1.next = curr2.next
        curr2.next = tmp
        prev2.next = curr1
    #printll(head)
    return head


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
# Read the link list elements including -1
arr = list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
m = int(input())
n = int(input())

l = swapTwoNodes(l, m, n)
printll(l)

'''
1 2 3 4 5 6 7 8 -1
2
5

1 2 3 4 5 -1
1
3

#Swap Head with something
1 2 3 4 5 6 7 8 -1
0
3

Swap adjacent nodes
1 2 3 4 5 6 7 8 -1
1
2

what if M > N ? first swap M,N
57 23 83 21 51 46 12 54 68 31 16 42 26 46 28 61 65 57 15 43 -1
3
2
'''