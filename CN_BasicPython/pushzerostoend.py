def pushzerostoend(arr, n):
    zeroloc = 0
    for i in range(n):
        if arr[i] != 0:
            arr[i], arr[zeroloc] = arr[zeroloc], arr[i]
            zeroloc += 1
    print(arr)


src = [0, 3, 0, 2, 0]
src1 = [9, 0, 0, 8, 2]
src2 = [0, 3, 0, 2, 0, 9, 0, 0, 8, 2]
src3 = [2, 6, 0, 0, 1, 9, 0, 8, 0]
#pushzerostoend(src, len(src))
#pushzerostoend(src1, len(src1))
#pushzerostoend(src2, len(src2))
pushzerostoend(src3, len(src3))
