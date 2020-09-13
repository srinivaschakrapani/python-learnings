import queue


def reverse(q1):
    if q1.qsize() == 0:
        return
    else:
        k = q1.get()
        reverse(q1)
        q1.put(k)


def reverseFirstK(q, k):
    if k == 0:
        return
    else:
        ele = q.get()
        r = k - 1
        reverseFirstK(q, r)
        q.put(ele)


from sys import setrecursionlimit

setrecursionlimit(11000)
n = int(input())
li = [int(ele) for ele in input().split()]
q = queue.Queue()
for ele in li:
    q.put(ele)
k = int(input())
reverse(q)
reverseFirstK(q, q.qsize() - k)
while (q.qsize() > 0):
    print(q.get())
    n -= 1
