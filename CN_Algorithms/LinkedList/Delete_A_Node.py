from sys import stdin

#Input format:
# 1 <Number of test cases>
# 3 4 5 2 6 1 9 -1
# 3 <position to delete>
# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def deleteNode_recursive(head, pos):
    if pos < 0:
        return head
    if head is None:
        return head
    if pos == 0:
        return head.next
    else:
        small_head = deleteNode_recursive(head.next, pos-1)
        head.next = small_head
        return head

def deleteNode(head, pos):
    prev = None
    curr = head
    dPos = 0
    list_len = lengthOfSLL(head)
    if curr is None or pos < 0 or pos >= list_len:
        return head
    else:
        while dPos != pos:
            prev = curr
            curr = curr.next
            dPos += 1
        # Delete head
        if prev is None:
            # curr = curr.next
            head = head.next
            return head
        else:
            prev.next = curr.next
            return head
    # Your code goes here


def lengthOfSLL(head):
    if head is None:
        return 0
    else:
        length = 0
        while head is not None:
            length += 1
            head = head.next
    return length


# Taking Input Using Fast I/O
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

def printReverse(head) :
    if head is None:
        return
    else:
        printReverse(head.next)
        print(head.data, end=" ")
        #return
    #Your code goes here

# main
#t = int(stdin.readline().strip())
head = takeInput()
#pos = int(stdin.readline().rstrip())
#pos = 2
#head = deleteNode_recursive(head, pos)
#printLinkedList(head)
printReverse(head)

# while t > 0:
#     head = takeInput()
#     pos = int(stdin.readline().rstrip())
#
#     head = deleteNode(head, pos)
#     printLinkedList(head)
#
#     t -= 1