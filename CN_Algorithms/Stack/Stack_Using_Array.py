class Stack:
    def __init__(self):
        self.__data = []
        self.data1 = [4, 5, 6, 7]

    def push(self, item):
        self.__data.append(item)
        print(len(self.__data))

    def pop(self):
        if not self.isEmpty():
            return self.__data.pop()
        print("Empty Stack !!")
        return

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return len(self.__data)

    def top(self):
        if not self.isEmpty():
            return self.__data[self.__data[len(self.__data) - 1]]
        print("Empty Stack !!")
        return


s = Stack()
#s.push(34)
#s.push(35)
s.push(36)

print(s.size())
#print(len(self.__data))
