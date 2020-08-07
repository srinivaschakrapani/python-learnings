def quicksort(arr, start, end):
    if start >= end:
        return
    else:
        pivotIndex = partition(arr, start, end)
        quicksort(arr, start, pivotIndex - 1)
        quicksort(arr, pivotIndex + 1, end)


def partition(arr, start, end):
    pivot = arr[start]
    k = 0
    for i in range(start, end + 1):
        if arr[i] < pivot:
            k += 1
    # pivot is swapped here
    arr[start + k], arr[start] = arr[start], arr[start + k]
    si = start
    ei = end
    while si < ei:
        if arr[si] < pivot:
            si += 1
        elif arr[ei] >= pivot:
            ei = ei - 1
        else:
            arr[si], arr[ei] = arr[ei],  arr[si]
            si += 1
            ei -= 1
    return start+k


src = [10, 9, 8, 7, 1, 3, 5, 4, 2]
quicksort(src, 0, len(src) - 1)
print(src)
