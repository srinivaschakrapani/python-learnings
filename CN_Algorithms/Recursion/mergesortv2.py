def merge_sort(a):
    if len(a) == 0 or len(a) == 1:
        return
    mid = len(a)//2

    a1 = a[:mid]
    a2 = a[mid:]
    merge_sort(a1)
    merge_sort(a2)
    merge(a1, a2, a)

def merge(a1, a2, a):




