arr1 = [2, 6, 1, 2]
n = 4
arr2 = [1,2,3,4,2]
m = 5
flst = []

len2 = m
for i in range(n):
    k = arr1[i]
    for j in range(len2):
        if k == arr2[j]:
            flst.append(k)
            for u in range(j, len2 - 1):
                arr2[u] = arr2[u + 1]
            len2 -= 1
            break
for s in flst:
    print(s, end=" ")
