import sys

sys.setrecursionlimit(1100)


def MultiplyRecursively(M, N):
    if N == 0:
        return 0
    else:
        return M + MultiplyRecursively(M, N - 1)


M = 1#int(input())
N = 1000#int(input())
print(MultiplyRecursively(M, N))
