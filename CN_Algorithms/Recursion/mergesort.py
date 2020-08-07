import math as mt
def mergesort(arr, start, end):
    if start < end:
        mid = mt.floor((start + end) // 2)
        mergesort(arr, start, mid)
        mergesort(arr, mid+1, end)
        merge(arr, start, end, mid)


def merge(arr, start, end, mid):
    print(f"Array : {arr}")
    lsubarr = arr[start:mid+1]
    len1 = len(lsubarr)

    rsubarr = arr[mid+1:end + 1]
    len2 = len(rsubarr)

    i = 0
    j = 0
    r = start
    while i < len1 and j < len2:
        if lsubarr[i] < rsubarr[j]:
            arr[r] = lsubarr[i]
            i += 1
        elif lsubarr[i] >= rsubarr[j]:
            arr[r] = rsubarr[j]
            j += 1
        r += 1
    while i < len1:
        arr[r] = lsubarr[i]
        i += 1
        r += 1

    while j < len2:
        arr[r] = rsubarr[j]
        j += 1
        r += 1


src = [6, 5, 3, 1, 8, 7, 2, 4]
print(f"Before Sorting: {src}")
mergesort(src, 0, len(src) - 1)
print(f"After Sorting: {src}")
