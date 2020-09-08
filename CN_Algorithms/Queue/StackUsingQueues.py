# Stack Using 2 Queues built in
from queue import *


class StackUsingQueues:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, data):
        self.q1.put(data)

    def pop(self):
        if self.q1.qsize() == 0:
            return -1
        elif self.q1.qsize() == 1:
            return self.q1.get()
        else:
            while self.q1.qsize() != 1:
                self.q2.put(self.q1.get())
            k = self.q1.get()
            while self.q2.qsize() != 0:
                self.q1.put(self.q2.get())

        return k

    def getSize(self):
        return self.q1.qsize()

    def top(self):
        if self.q1.qsize() == 0:
            return -1
        elif self.q1.qsize() == 1:
            k = self.q1.get()
            self.q1.put(k)
            return k
        else:
            while self.q1.qsize() != 1:
                self.q2.put(self.q1.get())
            k = self.q1.get()
            if self.q2.qsize() != 0:
                while self.q2.qsize() != 0:
                    self.q1.put(self.q2.get())
            self.q1.put(k)
        return k


s = StackUsingQueues()
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
        while s.q1.qsize() != 0:
            print(s.q1.get(), end=' ')

    i += 1
