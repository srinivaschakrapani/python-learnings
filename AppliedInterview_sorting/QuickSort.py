def quicksort(A, start, end):
    if start < end:
        q = partition(A, start, end)
        quicksort(A, start, q)
        quicksort(A, q + 1, end)
    print(f"After sorting {A}")


def partition(A, start, end):
    pv = start
    pivot = A[pv]
    i = start
    for j in range(i + 1, end):
        if A[j] > pivot:
            j += 1
        elif A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
            j += 1
    A[pv], A[i] = A[i], A[pv]
    # print(i)
    # print(f"After partition {A}")
    return i


if __name__ == '__main__':
    src = [6, 5, 3, 1, 8, 7, 2, 4]
    # src = [1, 2, 3, 4, 5, 6, 7, 8]
    print(f"Before Sorting {src}")
    quicksort(src, 0, len(src))
    # Partition(src, 0, len(src))
    # dest = BubbleSort(src)
    # print(f"After Sorting {QuickSort(src)}")
