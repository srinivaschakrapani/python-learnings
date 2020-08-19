# Find and return the equilibrium index of an array. Equilibrium
# index of an array is an index i such that the sum of elements at indices
# less than i is equal to the sum of elements at indices greater than i.
# Element at index i is not included in either part.
# If more than one equilibrium index is present, you need to return the
# first one. And return -1 if no equilibrium index is present.

def equilibriumIndex(arr):
    # Please add your code here
    index = 0
    leftsum = 0
    totalsum = 0
    for i in arr:
        totalsum += i

    while index < len(arr):
        rightsum = totalsum - arr[index] - leftsum
        if leftsum == rightsum:
            return index
        else:
            leftsum = leftsum + arr[index]
            index += 1
    return -1

# Main
n = int(input())
arr = [int(i) for i in input().strip().split()]
print(equilibriumIndex(arr))

#
# arr = [-7, 1, 5, 2, -4, 3, 0]
# print(equilibriumIndex(arr))
