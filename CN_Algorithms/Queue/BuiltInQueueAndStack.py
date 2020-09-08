import queue


def builtinstackandqueue():
    q = queue.Queue()
    q.put(5)
    q.put(4)
    q.put(3)
    q.put(2)
    print("Inbuilt Queue")
    while not q.empty():
        print(q.get())
    q = queue.LifoQueue()
    q.put(5)
    q.put(4)
    q.put(3)
    q.put(2)
    print("Inbuilt Queue")
    while not q.empty():
        print(q.get())



builtinstackandqueue()
