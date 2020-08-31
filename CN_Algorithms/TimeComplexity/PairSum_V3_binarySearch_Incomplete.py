from sys import stdin, setrecursionlimit


def BinarySearch(arr, start, end, key):
    # length = end - start + 1
    if start <= end:
        mid = (start + end) // 2
        if key == arr[mid]:
            return mid
        else:
            if key > arr[mid]:
                return BinarySearch(arr, mid + 1, end, key)
            elif key <= arr[mid]:
                return BinarySearch(arr, start, mid - 1, key)
    return -1


# # Naive method to find a pair in a list with given sum
# def findPair(A, sum):
#     # sort the list in ascending order
#     A.sort()
#
#     # maintain two indices pointing to end-points of the list
#     (low, high) = (0, len(A) - 1)
#
#     # reduce search space A[low..high] at each iteration of the loop
#
#     # loop till low is less than high
#     while low < high:
#
#         if A[low] + A[high] == sum:  # sum found
#             print(A[low], A[high])
#             print("Pair found")
#
#
#         # increment low index if total is less than the desired sum
#         # decrement high index is total is more than the sum
#         if A[low] + A[high] < sum:
#             low = low + 1
#         else:
#             high = high - 1
#
#     # No pair with given sum exists in the list
#     print("Pair not found")

def PairSum(arr, target):
    arr.sort()
    start = 0
    end = len(arr) - 1
    for i in range(start, end):
        key = target - arr[i]
        key_idx = BinarySearch(arr, i + 1, end, key)
        if key_idx != -1:
            print(arr[i], arr[key_idx])
            for k in range(key_idx - 1, -1, -1):
                if key == arr[k]:
                    print(arr[i], arr[k])
                else:
                    break
            for k in range(key_idx + 1, end + 1):
                if key == arr[k]:
                    print(arr[i], arr[k])
                else:
                    break


# arr = [1, 3, 6, 2, 5, 4, 3, 2, 4]
arr = [48, 11, 2, 16, 26, 7, 44, 29, 14, 5, 34, 23, 47, 43, 49, 36, 36, 6, 39, 43, 26, 44, 25, 17, 3, 18, 45, 4, 38, 10,
       19, 10, 45, 32, 18, 44, 30, 14, 5, 36, 23, 28, 34, 15, 36, 22, 50, 30, 14, 22, 32, 25, 36, 1, 8, 48, 14, 32, 9,
       34, 15, 31, 18, 32, 4, 3, 15, 17, 44, 48, 10, 39, 15, 15, 48, 7, 3, 11, 39, 21, 28, 35, 17, 38, 16, 42, 48, 6,
       18, 49, 40, 19, 35, 10, 22, 14, 37, 32, 3, 19, 50, 32, 9, 19, 45, 42, 40, 28, 9, 40, 42, 19, 43, 42, 41, 19, 50,
       10, 10, 15, 33, 49, 41, 9, 32, 13, 36, 11, 13, 50, 50, 46, 17, 39, 1, 22, 30, 39, 16, 16, 2, 8, 24, 43, 38, 7,
       48, 15, 29, 39, 21, 13, 4, 22, 18, 45, 50, 33, 43, 16, 28, 25, 6, 20, 47, 10, 15, 36, 19, 33, 6, 14, 12, 24, 19,
       18, 34, 39, 5, 41, 7, 27, 9, 33, 20, 25, 23, 4, 49, 32, 40, 28, 39, 2, 44, 9, 38, 18, 1, 27, 32, 17, 6, 11, 16,
       6, 25, 44, 34, 31, 3, 14, 15, 11, 48, 49, 18, 5, 47, 8, 19, 2, 40, 17, 7, 47, 11, 14, 47, 14, 31, 37, 7, 23, 32,
       17, 15, 48, 12, 20, 21, 12, 13, 42, 38, 15, 14, 26, 27, 25, 35, 43, 15, 32, 37, 12, 3, 7, 44, 14, 35, 18, 21, 49,
       9, 9, 39, 26, 17, 45, 39, 39, 24, 14, 6, 30, 6, 47, 16, 42, 42, 12, 10, 40, 49, 46, 26, 41, 34, 34, 47, 30, 3,
       33, 4, 7, 6, 7, 1, 16, 39, 34, 37, 34, 45, 4, 40, 43, 48, 22, 23, 20, 50, 10, 7, 20, 45, 43, 47, 47, 19, 15, 27,
       44, 8, 18, 21, 8, 3, 41, 2, 43, 17, 41, 4, 47, 45, 18, 49, 41, 3, 41, 14, 16, 23, 1, 24, 2, 9, 6, 31, 5, 35, 25,
       50, 36, 34, 26, 29, 45, 39, 47, 44, 5, 34, 1, 8, 7, 48, 17, 10, 13, 5, 31, 38, 27, 22, 36, 32, 21, 11, 27, 16, 5,
       31, 30, 6, 35, 20, 47, 15, 23, 50, 14, 11, 20, 5, 31, 12, 15, 1, 4, 5, 36, 16, 2, 38, 10, 12, 28, 1, 12, 22, 34,
       19, 1, 37, 13, 31, 20, 16, 26, 21, 34, 40, 31, 3, 12, 28, 19, 49, 3, 5, 2, 12, 42, 33, 12, 32, 12, 45, 9, 32, 3,
       30, 38, 28, 16, 7, 8, 2, 4, 34, 31, 42, 41]
# setrecursionlimit(1000)
PairSum(arr, 90)
# findPair(arr,7)
