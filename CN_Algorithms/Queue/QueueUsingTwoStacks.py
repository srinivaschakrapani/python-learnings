class QueueUsingTwoStacks:
    def __init__(self):
        self.__s1 = []
        self.__s2 = []

    def enqueue(self, data):
        self.__s1.append(data)

    def getSize(self):
        return len(self.__s1)

    def isEmpty(self):
        return self.getSize() == 0

    def printQueue(self):
        for i in self.__s1:
            print(i)

    def dequeue(self):
        while (len(self.__s1)) != 0:
            self.__s2.append(self.__s1.pop())
        k = self.__s2.pop()

        while (len(self.__s2)) != 0:
            self.__s1.append(self.__s2.pop())
        print("Popped k ==> " + str(k))
        return k


q = QueueUsingTwoStacks()
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.printQueue()
q.dequeue()
q.printQueue()