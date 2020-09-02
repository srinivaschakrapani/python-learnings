class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def Swap(node1, node2):
    tmp = node2.next
    node2.next = node1
    node1.next = tmp
    return node2

def bubbleSortLL(head):
    if head is None or head.next is None:
        return head
    len_ll = length(head)
    prev = None
    curr = head

    i = 0
    for i in range(len_ll):
        prev = None
        curr = head
        while curr is not None and curr.next is not None:
            if curr.data > curr.next.data:
                if prev is None:
                    tmp = curr.next
                    curr.next = tmp.next
                    tmp.next = curr
                    # head = tmp
                    curr = head = tmp
                else:

                    # Swap the nodes
                    # tmp = curr
                    # prev.next = curr.next
                    # curr.next = curr.next.next
                    # prev.next.next = curr
                    # curr = tmp
                    prev.next = Swap(curr, curr.next)


            printll(head)
            prev = curr
            curr = curr.next
    printll(head)
            # len_ll -= 1
            # i = 0





    while curr is not None:
        after = curr.next


def length(head):
    if head is None:
        return 0
    else:
        i = 0
        curr = head
        while curr is not None:
            i += 1
            curr = curr.next
    return i
def ll(arr):
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    i = 1
    tail = head
    while i < len(arr):
        nn = Node(arr[i])
        tail.next = nn
        tail = nn
        i += 1
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
l = bubbleSortLL(l)
printll(l)




