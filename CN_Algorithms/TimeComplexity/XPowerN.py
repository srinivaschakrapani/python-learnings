def XPowerN(x, n):
    if n == 0:
        return 1
    small_power = XPowerN(x, n // 2)
    if n % 2 == 0:
        return small_power * small_power
    else:
        return small_power * small_power * x


x, n = list(int(i) for i in input().strip().split(' '))
print(XPowerN(x, n))
