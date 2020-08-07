def binarysearch(arr, x, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2
    if x == arr[mid]:
        return mid
    elif x > arr[mid]:
        return binarysearch(arr, x, mid + 1, end)
    else:
        return binarysearch(arr, x, start, mid - 1)


s = [1, 2, 3, 4, 5, 6]  # abcba
print(binarysearch(s, 4, 0, len(s) - 1))
