def MergeSort(a):
    if len(a) == 0 or len(a) == 1:
        return
    mid = len(a) // 2
    a1 = a[0:mid]
    a2 = a[mid:]
    MergeSort(a1)
    MergeSort(a2)
    Merge(a1, a2, a)


def Merge(a1, a2, a):
    i = 0
    j = 0
    k = 0
    print("Intermediate Input -->", a)
    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            a[k] = a1[i]
            k += 1
            i += 1
        else:
            a[k] = a2[j]
            k += 1
            j += 1
    while i < len(a1):
        a[k] = a1[i]
        i += 1
        k += 1
    while j < len(a2):
        a[k] = a2[j]
        k += 1
        j += 1
    print("Intermediate output -->", a)


arr = [5, 4, 3, 2, 1]
print(arr)
MergeSort(arr)
print(arr)
