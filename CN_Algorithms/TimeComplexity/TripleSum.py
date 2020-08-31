from sys import stdin
#Time complexity  : O(N^3)
#Space Complexity : O(1)

def TripleSum(arr, target):
    arr.sort()
    for i in range(len(arr) - 2):
        for j in range(i + 1, len(arr) - 1):
            for k in range(j + 1, len(arr)):
                if arr[i] + arr[j] + arr[k] == target:
                    print(arr[i], arr[j], arr[k])


# def takeInput():
#     n = int(stdin.readline().rstrip())
#     if n == 0:
#         return list(), 0
#
#     arr = list(map(int, stdin.readline().rstrip().split(" ")))
#     return arr, n
#
#
# arr, N = takeInput()
# target = int(input())
# TripleSum(arr, target)

A = [1, 2, 3, 4, 5, 6, 7]
target = 12
TripleSum(A, target)
