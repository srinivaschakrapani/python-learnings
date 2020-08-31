# Even nodes after Odd nodes in  a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def arrange_LinkedList(head):
    #  Even after Odd LinkedList: Arrange elements in a given Linked List such
    #  that, all even numbers are placed after odd numbers. Respective order of
    #  elements should remain same.
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if head is None or head.next is None:
        return head

    evenhead = eventail = None
    oddhead = oddtail = None
    curr = head
    while curr is not None:
        tail = curr.next
        if curr.data % 2 == 0:
            if evenhead is None:
                evenhead = eventail = curr
                eventail.next = None
            else:
                eventail.next = curr
                eventail = curr
                eventail.next = None
        else:
            if oddhead is None:
                oddhead = oddtail = curr
                oddtail.next=None
            else:
                oddtail.next = curr
                oddtail = curr
                oddtail.next = None
        curr = tail
    #Everything is even
    if oddhead is None:
        #printll(evenhead)
        return evenhead
    elif evenhead is None:
        #printll(oddhead)
        return oddhead
    else:
        # First ODD followed by even
        oddtail.next = evenhead
        eventail.next = None
        printll(oddhead)










def ll(arr):
    if len(arr)==0:
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
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
l = arrange_LinkedList(l)
printll(l)

