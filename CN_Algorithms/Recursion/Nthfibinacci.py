# Nth Fibonacci number
# 1 1 2 3 5 8 13 ...
def nthfibonacci(n):
    if n == 1 or n == 2:
        return 1
    output = nthfibonacci(n - 1) + nthfibonacci(n - 2)
    return output


print(nthfibonacci(6))
