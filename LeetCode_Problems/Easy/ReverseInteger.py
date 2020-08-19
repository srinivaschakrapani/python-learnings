from math import fabs
class Solution:
    def reverse(self, x: int) -> int:
        if x < -2 ** 31 or x > 2 ** 31 - 1:
            return 0
        t = fabs(x)
        r = self.reverseDigits(t)
        if t < -2 ** 31 or t > 2 ** 31 - 1:
            return 0

        if x < 0:
            return -t
        return t

    def reverseDigits(self, x):
        if x < 10:
            return x
        else:
            q = x // 10
            rem = x % 10
            small_output = rem * (10 ** len(str(q)))
            return small_output + self.reverseDigits(q)


#1534236469
#2147483648
s = Solution()
inp = -123
# isNegative = False
# if inp < 0:
#     isNegative = True
#     inp *= -1
res = s.reverse(inp)
# if isNegative:
#     res *= -1
print(res)
#2147483648