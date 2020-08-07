def checkNumber(arr, x):
    # Please add your code here
    arr_len = len(arr)
    if arr_len == 1:
        return x == arr[0]
    elif x == arr[0]:
        return True
    else:
        return checkNumber(arr[1:], x)


# Main
from sys import setrecursionlimit

setrecursionlimit(11000)
n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
x = int(input())

if checkNumber(arr, x):
    print('true')
else:
    print('false')
