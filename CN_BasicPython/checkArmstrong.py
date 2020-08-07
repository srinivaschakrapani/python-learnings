def checkArmstrong(n):
    sum = 0
    dc = numberOfDigits(n)
    i = n
    while i > 0:
        k = i % 10
        sum = sum + k ** dc
        i = i // 10
    if sum == n:
        return True
    else:
        return False


def numberOfDigits(n):
    return len(str(n))


n = int(input())
print(checkArmstrong(n))
