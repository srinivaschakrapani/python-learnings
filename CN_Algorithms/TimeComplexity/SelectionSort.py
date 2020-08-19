def SelectionSort(a):
    l = len(a)
    for i in range(l):
        min_idx = i
        for j in range(i+1,l):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
        #print("Intermediate Output: ", a)
#arr = [10,8,9,4,6,1,3,2]
#SelectionSort(arr)
#print(arr)