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
    # Find all elements less than k
    for i in range(start, end + 1):
        if arr[i] < pivot:
            k += 1

    # pivot is swapped to the kth position element
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
    print(arr)
    return start+k


src = [2, 6, 8, 5, 4, 3, 2]#[10, 9, 8, 7, 1, 3, 5, 4, 2]
quicksort(src, 0, len(src) - 1)
print(src)
