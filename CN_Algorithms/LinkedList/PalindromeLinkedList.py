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


# def lengthOfSLL(head):
#     if head is None:
#         return 0
#     else:
#         length = 0
#         while head is not None:
#             length += 1
#             head = head.next
#     return length

def midOfSLL(head):
    if head is None or head.next is None:
        return 0
    if head.next.next is None:
        return 1
    else:
        slow = fast = head
        cnt = 0
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
            #cnt += 1
        #print(cnt)
        return slow

# to print the linked list
def printLinkedList(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print()


def isPalindrome(head):
    if head is None or head.next is None:
        return True
    tail1 = midOfSLL(head)
    head1 = head
    head2 = tail1.next
    tail1.next = None
    second_half = reverseLinkedList(head2, None)
    # print(head1)
    # print(head2)

    while head1 is not None and second_half is not None:
        if head1.data == second_half.data:
            head1 = head1.next
            second_half = second_half.next
            continue
        else:
            # return False
            print("Not Palindrome")
            break
    else:
        # return True
        print("Palindrome")
    # printLinkedList(h1)
    # printLinkedList(head2)


def InsertANode(head, value):
    if head is None:
        head = Node(value)
        head.next = None
    else:
        k = head
        while k.next is not None:
            k = k.next
        k.next = Node(value)
    return head


def reverseLinkedList(head, newhead):
    if head is None:
        return newhead
    else:
        next = head.next
        head.next = newhead
        newhead = head
        head = next
        return reverseLinkedList(head, newhead)

def reverseLinkedList_iterative(head):
    if head is None:
        return head
    else:
        prev = None
        curr = head
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        printLinkedList(prev)

head = takeInput()
# newhead = reverseLinkedList(head, None)
# printLinkedList(newhead)
#isPalindrome(head)
#reverseLinkedList_iterative(head)
H1 = reverseLinkedList(head, None)
printLinkedList(H1)
#midOfSLL(head)
#printLinkedList(head)
