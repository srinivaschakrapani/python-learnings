def lastindex(arr, x):
    arr_len = len(arr)
    if arr_len == 0:
        return -1

    sublist = lastindex(arr[1:], x)
    if sublist != -1:
        return sublist + 1
    else:
        if arr[0] == x:
            return 0
        else:
            return -1

def lastindexv2(arr, x, start):
    arr_len = len(arr)
    if start == arr_len:
        return -1

    sublist = lastindexv2(arr, x, start + 1)
    if sublist != -1:
        return sublist
    else:
        if arr[start] == x:
            return start
        else:
            return -1


arr = [1, 2, 3, 2, 4]
print(lastindex(arr, 2))
print(lastindexv2(arr, 2, 0))

# # Main
# from sys import setrecursionlimit
#
# setrecursionlimit(11000)
# n = int(input())
# arr = list(int(i) for i in input().strip().split(' '))
# x = int(input())
# print(firstIndex(arr, x, 0))