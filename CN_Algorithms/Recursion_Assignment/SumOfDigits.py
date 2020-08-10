def SumOfDigits(number):
    if number >= 0 and number < 10:
        return number
    else:
        smallnumber = number // 10
        return (number % 10) + SumOfDigits(smallnumber)


num = 12345
res = SumOfDigits(num)
print(res)
