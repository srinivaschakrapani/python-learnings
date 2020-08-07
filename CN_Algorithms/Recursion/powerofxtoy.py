from sys import stdin


def powerxtoy(x, y):
    if y == 0:
        return 1
    return x * powerxtoy(x, y - 1)


arr = stdin.readline().rstrip().split(" ")

base, exp = int(arr[0]), int(arr[1])
print(powerxtoy(base, exp))
