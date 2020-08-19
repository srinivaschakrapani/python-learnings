# Given two random integer arrays, print their intersection.
# That is, print all the elements that are present in both the given arrays.
# Input arrays can contain duplicate elements.
# Sample Input 1 :
# 6
# 2 6 8 5 4 3
# 4
# 2 3 4 7
# Sample Output 1 :
# 2
# 4
# 3
def intersection(arr1, arr2):
    QuickSort(arr1, 0, len(arr1) - 1)
    QuickSort(arr2, 0, len(arr2) - 1)
    if len(arr1) > len(arr2):
        arr1, arr2 = arr2, arr1
    PrintIntersection(arr1, arr2)


def PrintIntersection(arr1, arr2):
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            print(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1


def QuickSort(arr, start, end):
    if start < end:
        p_Index = Partition(arr, start, end)
        QuickSort(arr, start, p_Index - 1)
        QuickSort(arr, p_Index + 1, end)


def Partition(a, st, end):
    pivot = a[st]
    k = 0
    for p in range(st, end + 1):
        if a[p] < pivot:
            k += 1
    a[st + k], a[st] = a[st], a[st + k]

    i = st
    j = end

    while i < j:
        if a[i] < pivot:
            i += 1
        elif a[j] >= pivot:
            j -= 1
        else:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
    return st + k

# Main
n1 = int(input())
arr1 = list(int(i) for i in input().strip().split(' '))
n2 = int(input())
arr2 = list(int(i) for i in input().strip().split(' '))
intersection(arr1, arr2)

#Test
#arr1 = [2, 6, 8, 5, 4, 3, 2]
#arr2 = [2, 3, 4, 7, 2]
#intersection(arr1, arr2)
# QuickSort(arr1, 0, len(arr1) - 1)
# print(arr1)
