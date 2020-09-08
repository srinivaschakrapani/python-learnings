# Reverse a given Stack with the help of another empty stack.
# Two stacks will be given. Out of which first contains some integers
# and second one is empty. You need to reverse the first one using second stack.
# Change in the given first stack itself.

def reverseStack(s1, s2):
    if len(s1) <= 1:
        return
    else:
        while len(s1) != 1:
            s2.append(s1.pop())
        top = s1.pop()
        while len(s2) != 0:
            s1.append(s2.pop())
        reverseStack(s1, s2)
        s1.append(top)


#### Implement the code here

from sys import setrecursionlimit

setrecursionlimit(11000)
n = int(input())
s1 = [int(ele) for ele in input().split()]
s2 = []
reverseStack(s1, s2)
while (len(s1) != 0):
    print(s1.pop(), end=' ')
