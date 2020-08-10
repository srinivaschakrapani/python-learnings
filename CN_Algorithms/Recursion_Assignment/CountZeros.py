def CountZeros(number):
    if number == 0:
        return 1
    elif number > 0 and number < 10:
        return 0
    else:
        smallnum = number // 10
        remainder = number % 10
        if remainder == 0:
            return 1 + CountZeros(smallnum)
        else:
            return CountZeros(smallnum)

num = int(input())
print(CountZeros(num))
