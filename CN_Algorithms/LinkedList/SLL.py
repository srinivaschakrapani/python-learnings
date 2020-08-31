# Single Linked List
# Reading Input Naive approach O(N^2)
# Smart approach with O(N)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertAtIthPosition_Recursive(head, data, i):
    if i < 0:
        return head
    if head is None:
        return
    if i == 0:
        nn = Node(data)
        nn.next = head
        return nn
    small_head = insertAtIthPosition_Recursive(head.next, data, i-1)
    head.next = small_head
    return head


# Insert at Ith Position
def insertAtIthPosition(head, nn, i):
    if i < 0 or i > lengthOfSLL(head):
        printSLL(head)
    prev = None
    curr = head
    nodepos = 0
    while curr is not None:
        if nodepos == i:
            if prev is None:
                nn.next = head
                head = nn
            else:
                nn.next = curr
                prev.next = nn
            break
        prev = curr
        curr = curr.next
        nodepos += 1
    printSLL(head)


# Print Ith Node
def printIthNode(head, i):
    if head is None:
        return
    else:
        start = 0
        temp = head
        while temp is not None:
            if start == i:
                return temp.data
            start += 1
            temp = temp.next
        return


def takeinput_LinearTime():
    head = tail = None
    inp = [int(ele) for ele in input().split(' ')]
    for currData in inp:
        if currData == -1:
            break
        else:
            if head is None:
                head = tail = Node(currData)
            else:
                nn = Node(currData)
                tail.next = nn
                tail = nn
    return head


# Time Complexity : O(N^2)
def takeinput():
    head = None
    inp = [int(ele) for ele in input().split(' ')]
    for currData in inp:
        if currData == -1:
            break
        else:
            if head is None:
                head = Node(currData)
            else:
                nn = Node(currData)
                k = head
                while k.next is not None:
                    k = k.next
                k.next = nn
    return head


def printSLL(head):
    if head is None:
        return
    else:
        k = head
        while k is not None:
            print(k.data, " ->", end=' ')
            k = k.next
        print("None", end=' ')

def lengthOfSLL(head):
    if head is None:
        return 0
    else:
        count = 0
        while head is not None:
            count +=1
            head = head.next
    return count
# head  = takeinput()
head = takeinput_LinearTime()
# print(printIthNode(head, 3))
# insertAtIthPosition(head, Node(91), 3)
# insertAtIthPosition(head, Node(89), 0)
printSLL(head)
insertAtIthPosition_Recursive(head, 91, 20)
print()
printSLL(head)
# insertAtIthPosition_Recursive(head, 89, 0)
# printSLL(head)
# printSLL(head)
