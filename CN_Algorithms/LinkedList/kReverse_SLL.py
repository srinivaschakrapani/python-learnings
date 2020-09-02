class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def kReverse(head, n):
    #  Implement kReverse( k ) in a linked list i.e. you need to reverse
    #  first K elements then reverse next k elements and join the linked list and
    #  so on. Indexing starts from 0. If less than k elements left in the last,
    #  you need to reverse them as well. If k is greater than length of LL,
    #  reverse the complete LL. If n is 4 and LL is:
    #  Input: 1 2 3 4 5 6 7 8 9 10
    #  Output: 4 3 2 1 8 7 6 5 10 9
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if head is None or head.next is None:
        return head
    len_list = len_sll(head)

    if n > len_list:
        h, t = reverse_a_sll(head)
        return h
    i = 1

    tail1 = head1 = head
    while i != n:
        tail1 = tail1.next
        i += 1
    nxt_head = tail1.next
    tail1.next = None
    head1, tail1 = reverse_a_sll(head1)
    tail1.next = kReverse(nxt_head, n)
    return head1


def reverse_a_sll(head):
    prev = None
    curr = head
    tail = head
    while curr is not None:
        nxt = curr.next
        curr.next = prev
        # prev.next = nxt
        prev = curr
        curr = nxt
    return prev, tail


def len_sll(head):
    cnt = 0
    if head is None:
        return 0
    else:
        curr = head
        while curr is not None:
            cnt += 1
            curr = curr.next
    return cnt


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
i = int(input())
l = kReverse(l, i)
printll(l)
