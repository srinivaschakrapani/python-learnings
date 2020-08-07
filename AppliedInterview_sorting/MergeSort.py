import math as mt
# Merge Sort
def MergeSort(A, p, q):
    if (p < q):
        r = mt.floor((p + q) / 2)
        # print(f"{p} -> {q}")
        MergeSort(A, p, r)
        # print(f"{r+1} -> {q}")
        MergeSort(A, r + 1, q)
        Merge(A, p, q, r)

# Merge the subarrays
def Merge(A, p, q, r):
    print(f"Array : {A}")
    l1 = r - p + 1
    l2 = q - r

    L = A[p:r + 1]
    R = A[r + 1:q + 1]

    j = 0
    k = 0
    i = p
    #print(f"i, j, k, {i, j, k}")
    # print(f"p, q, r {p,q,r}")
    # print(f"l1, l2 = {l1,l2}")
    #print(f"Left = {L} Right = {R}")
    # print(f"{j,k}")

    while (j < l1 and k < l2):
        if L[j] < R[k]:
            # B.append(L[j])
            A[i] = L[j]
            # B[i] = L[j]
            j += 1
            # print(f" j, k = * {j,k}")
        elif L[j] >= R[k]:
            #B.append(R[k])
            A[i] = R[k]
            k += 1
        i += 1
    while (j < l1):
        A[i] = L[j]
        #B.append(L[j])
        j += 1
        i += 1

    while (k < l2):
        A[i] = R[k]
        #B.append(L[k])
        k += 1
        i += 1

if __name__ == '__main__':
    print("Hello")
    src = [6, 5, 3, 1, 8, 7, 2, 4]
    print(f"Before Sorting: {src}")
    MergeSort(src, 0, len(src) - 1)
    print(f"After Sorting: {src}")