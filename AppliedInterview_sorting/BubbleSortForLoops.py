from random import randint

#V1
def bubbleSortEnhanced(arr, n):
    # Your code goes here
    swaps = 0
    iters = 0
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
            iters +=1
        iters += 1

    print(f" Swaps enhanced {swaps}")
    print(f" iterations enhanced {iters}")
    return arr

#V2
def bubbleSort(arr, n):
    # Your code goes here
    k = n
    swap = True
    swaps = 0
    iters = 0
    while swap:
        swap = False
        i = 1
        while i < k:
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                swap = True
                swaps += 1
            i += 1
            iters +=1
        k -= 1
        iters +=1
    print(f" Swaps non enahnced {swaps}")
    print(f" iterations NON enhanced {iters}")
    return arr


if __name__ == '__main__':
    # src = [6, 5, 3, 1, 8, 7, 2, 4]
    # src = [99,2,4,1,3,6,13,28]
    #src = [1,2,3,4,5,6,7,8]
    src =[]
    for i in range(1, 1000):
        src.append(randint(1, 1000))
    # src = [1, 2, 3, 4, 5, 6, 7, 8]
    src1 = src.copy()
    print(f"Before Sorting {src}")
    # dest = BubbleSort(src)
    print(f"After Sorting {bubbleSort(src, len(src))}")#247109
    print(f"Before Sorting {src1}")
    # dest = BubbleSort(src)
    print(f"After Sorting {bubbleSortEnhanced(src1, len(src1))}")
