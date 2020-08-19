def QuickSort(A, start, end):
    if start < end:
        pIndex = Partition(A, start, end)
        QuickSort(A, start, pIndex - 1)
        QuickSort(A, pIndex + 1, end)


def Partition(A, start, end):
    pivot = A[end]
    pIndex = start
    for i in range(start, end):
        if A[i] <= pivot:
            A[i], A[pIndex] = A[pIndex], A[i]
            pIndex += 1
    A[pIndex], A[end] = A[end], A[pIndex]
    return pIndex


a = [7, 2, 4, 1, 5, 3]
#a = [4, 3, 2, 1]
QuickSort(a, 0, len(a) - 1)
print(a)
