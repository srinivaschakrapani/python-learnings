def merge(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    res = []
    i = 0
    j = 0
    while i < n1 and j < n2:
        if arr1[i] <= arr2[j]:
            res.append(arr1[i])
            i+=1
        else:
            res.append(arr2[j])
            j +=1
    if i < n1 :
        for k in range(i,n1):
            res.append(arr1[i])
    if j < n2:
        for k in range(j,n2):
            res.append(arr2[j])
    print(res)

#merge([1,5,7,9,11], [2,3,8,13])
merge([1,5,7,9,11], [])