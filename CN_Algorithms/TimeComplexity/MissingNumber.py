# Given an array of integers of size n which contains numbers
# from 0 to n - 2. Each number is present at least once.
# That is, if n = 5, numbers from 0 to 3 is present in the given array at least once
# and one number is present twice.
# You need to find and return that duplicate number present in the array.
# Assume, duplicate number is always present in the array.
def MissingNumber(arr):
    arrsum = 0
    for i in arr:
        arrsum += i
    n = max(arr)
    totalSum = int(n * (n + 1) / 2)
    return arrsum - totalSum


arr = [0]
print(MissingNumber(arr))
