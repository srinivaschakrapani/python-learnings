def binarySearch(arr, n, x) :
    start = 0
    end = n-1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == x:
            return mid
        elif x > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    else:
        return -1
def binarySearchRecursive(arr,start,end,x) :
    st = start
    e = end
    mid = (start + end) //2
    if start > end:
        return -1
    elif arr[mid] == x:
        return mid
    elif x > arr[mid]:
        return binarySearchRecursive(arr,mid+1,end,x)
    else:
        return binarySearchRecursive(arr[:mid-2], x)

arr = [1,3,7,9,11,12,45]
#print(binarySearch(arr,len(arr),3))
#print(binarySearch(arr,len(arr),12))
#print(binarySearch(arr,len(arr),45))
#print(binarySearch(arr,len(arr),1))
print(binarySearchRecursive(arr,12))
print(binarySearchRecursive(arr,45))
print(binarySearchRecursive(arr,1))