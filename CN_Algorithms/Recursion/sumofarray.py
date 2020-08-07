def sumArray(arr):
    # Please add your code here
    arr_size = len(arr)
    if arr_size == 0:
        return 0;
    else:
        sum = arr[0] + sumArray(arr[1:])
        return sum


# Main
from sys import setrecursionlimit

setrecursionlimit(11000)
n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
print(sumArray(arr))
