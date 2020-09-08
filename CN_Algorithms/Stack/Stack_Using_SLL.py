###Following Node class us already created internally. You can directly use that.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class StackUsingLL:
    ### Implement all these functions here

    def __init__(self):
        self.__head = None
        self.__size = 0

    def push(self, data):
        if self.__head is None:
            self.__head = Node(data)
            self.__size += 1
        else:
            nn = Node(data)
            nn.next = self.__head
            self.__head = nn
            self.__size += 1

    def pop(self):
        if not self.isEmpty():
            temp = self.__head
            self.__head = self.__head.next
            self.__size -= 1
            return temp.data
        return 0

    # Return 0 if stack is empty. Don't display any other message
    def top(self):
        if not self.isEmpty():
            return self.__head.data
        return 0

    # Return 0 if stack is empty. Don't display any other message
    def isEmpty(self):
        return self.getSize() == 0

    def getSize(self):
        return self.__size


s = StackUsingLL()
li = [int(ele) for ele in input().split()]
i = 0
while i < len(li):
    choice = li[i]
    if choice == -1:
        break
    elif choice == 1:
        s.push(li[i + 1])
        i += 1
    elif choice == 2:
        ans = s.pop()
        if ans != 0:
            print(ans)
        else:
            print(-1)
    elif choice == 3:
        ans = s.top()
        if ans != 0:
            print(ans)
        else:
            print(-1)
    elif choice == 4:
        print(s.getSize())
    elif choice == 5:
        if (s.isEmpty()):
            print('true')
        else:
            print('false')
    i += 1


