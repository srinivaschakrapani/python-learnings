def StringToInt(number):
    if len(number) == 1:
        return ord(number) - 48
    else:
        num = ord(number[0]) - 48
        smallproblem = number[1:]  # Let recursion handle this
        # 1234 , len(1234) = 4
        # 1 * (10**(4-1)) + StringToInt(smallproblem) # Recursive call
        return num * (10 ** (len(number) - 1)) + StringToInt(smallproblem)


num = input()
res = StringToInt(num)
print(res, type(res))
