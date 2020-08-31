class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def mid_of_sll(head):
    if head is None or head.next is None:
        return head
    else:
        slow = fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow


def merge(head1, head2):
    newhead = newtail = None
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    else:
        if head1.data <= head2.data:
            newhead = head1
            head1 = head1.next
        else:
            newhead = head2
            head2 = head2.next
        newhead.next = newtail #connect head and tail
        newtail = newhead

        while head1 is not None and head2 is not None:
            if head1.data <= head2.data:
                newtail.next = head1
                newtail = head1
                head1 = head1.next
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
        return newhead


def mergeSort(head):
    #  Sort a given linked list using Merge Sort.

    # base condition
    if head is None or head.next is None:
        return head
    mid = mid_of_sll(head)
    h2 = mid.next
    mid.next = None
    left = mergeSort(head)
    right = mergeSort(h2)
    return merge(left, right)

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
l = mergeSort(l)
printll(l)
'''
1 4 5 2 -1
'''
