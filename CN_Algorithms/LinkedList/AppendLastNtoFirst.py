from sys import stdin


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def takeInput():
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1):
        data = datas[i]
        newNode = Node(data)

        if head is None:
            head = newNode
            tail = newNode

        else:
            tail.next = newNode
            tail = newNode

        i += 1

    return head


# to print the linked list
def printLinkedList(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print()


def appendLastNToFirst(head, n):
    len_list = lengthOfSLL(head)
    if n > len_list or n == 0:
        return head
    cnt = len_list- n
    i = 0
    prev = curr = head
    while i < cnt:
        prev = curr
        curr = curr.next
        i += 1
    prev.next = None

    head2 = curr
    while curr.next != None:
        curr = curr.next
    tail2 = curr

    tail2.next = head
    return head2


def lengthOfSLL(head):
    if head is None:
        return 0
    else:
        length = 0
        while head is not None:
            length += 1
            head = head.next
    return length


head = takeInput()
# 1 2 3 4 5 -1
printLinkedList(head)
head2 = appendLastNToFirst(head, 4)
printLinkedList(head2)
