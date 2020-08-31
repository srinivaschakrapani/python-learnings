#TimeComplexity O(N^2)
#Space Complexity O(1)

def PairSum(A, x):
    #A.sort()
    for i in range(len(A) - 1):
        for j in range(i + 1, len(A)):
            if A[i] + A[j] == x:
                print(A[i], A[j])

# arr = [1, 3, 6, 2, 5, 4, 3, 2, 4]
# PairSum(arr, 7)
# # arr = [2, 2, 2]
