class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def merge(head1,head2):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    # two linked lists sorted in increasing order. Merge them in such
    # a way that the result list is also sorted (in increasing order). Try
    # solving with O(1) auxiliary space (in-place). You just need to return the
    # head of new linked list, don't print the elements.

    newhead = newtail = None
    if head1.data <= head2.data:
        newhead = head1
        head1 = head1.next
    else:
        newhead = head2
        head2 = head2.next
    newhead.next = newtail
    newtail = newhead

    while head1 is not None and head2 is not None:
        if head1.data <= head2.data:
            if newtail is None:
                newtail = head1
                newhead.next = newtail
            else:
                newtail.next = head1
                newtail = head1
            head1 = head1.next
        else:
            if newtail is None:
                newtail = head2
                newhead.next = newtail
            else:
                newtail.next = head2
                newtail = head2
            head2 = head2.next

    while head1 is not None:
        newtail.next = head1
        newtail = head1
        head1 = head1.next

    while head2 is not None:
        newtail.next = head2
        newtail = head2
        head2 = head2.next
    #print(newhead)
    return newhead


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
arr1=list(int(i) for i in input().strip().split(' '))
arr2=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l1 = ll(arr1[:-1])
l2 = ll(arr2[:-1])
l = merge(l1, l2)
printll(l)

''' 
2 5 8 12 -1
3 6 9 -1
'''
'''
2 2 3 -1
3 4 -1
'''
'''
1636 -1
90761 -1
'''
