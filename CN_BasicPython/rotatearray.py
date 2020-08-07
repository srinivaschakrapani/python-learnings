def rotate(arr, n, d):
    # Your code goes here
    l = []
    if d == 0:
        return
    else:
        for i in range(d, n):
            l.append(arr[i])
        for k in range(d):
            l.append(arr[k])
    for k in range(n):
        arr[k] = l[k]


arr = [1, 2, 3, 4]
n = len(arr)
d = 2
print('Fucntion call')
rotate(arr, n, d)
print(arr)
