def firstIndex(arr, x, currIndex):
    # Please add your code here
    arr_len = len(arr)
    if arr_len == 1:
        if x != arr[0]:
            return -1
        return 0
    if x == arr[0]:
        return currIndex
    return firstIndex(arr[1:], x, currIndex + 1)

def firstIndexversion2(arr, x):
    # Please add your code here
    arr_len = len(arr)
    if arr_len == 0:
        return -1
    if arr[0] == x:
        return 0
    smalllist = arr[1:]
    smallerListOutput = firstIndexversion2(smalllist, x)
    if smallerListOutput == -1:
        return -1
    else:
        return smallerListOutput + 1

def firstIndexversion3(arr, x, start):
    # Please add your code here
    arr_len = len(arr)
    if start == arr_len:
        return -1
    if arr[start] == x:
        return start

    return firstIndexversion2(arr, x, start + 1)


# # Main
# from sys import setrecursionlimit
#
# setrecursionlimit(11000)
# n = int(input())
# arr = list(int(i) for i in input().strip().split(' '))
# x = int(input())
# print(firstIndex(arr, x, 0))

