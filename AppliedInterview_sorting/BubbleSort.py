from random import randint
def BubbleSort(src):
    k = len(src)
    swap = True
    while swap:
        swap = False
        i = 1
        while i < k:
            if src[i - 1] > src[i]:
                src[i - 1], src[i] = src[i], src[i - 1]
                swap = True
            i += 1
        k -= 1
    return src


if __name__ == '__main__':
    #src = [6, 5, 3, 1, 8, 7, 2, 4]
    #src = [99,2,4,1,3,6,13,28]
    src = []
    for i in range(1,1000):
        src.append(randint(1,1000))
    #src = [1, 2, 3, 4, 5, 6, 7, 8]
    print(f"Before Sorting {src}")
    # dest = BubbleSort(src)
    print(f"After Sorting {BubbleSort(src)}")
