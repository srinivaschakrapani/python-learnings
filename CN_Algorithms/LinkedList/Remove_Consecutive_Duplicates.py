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

def removeConsecutiveDuplicates(head):
    if head is None:
        return head
    if head.next is None:
        return head
    else:
        prev = head
        nxt = head.next
        while nxt is not None:
            if prev.data != nxt.data:
                prev = nxt 
                nxt = nxt.next
            while nxt is not None and prev.data == nxt.data:
                nxt = nxt.next
            else:
                prev.next = nxt
    printLinkedList(head)

# to print the linked list
def printLinkedList(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print()

head = takeInput()
removeConsecutiveDuplicates(head)