# A child is running up a staircase with N steps, and can hop
# either 1 step, 2 steps or 3 steps at a time.
# Implement a method to count how many
# possible ways the child can run up to the stairs.
# You need to return number of possible ways W.
def Staircase(N):
    if N == 1 or N == 0:
        return 1
    elif N == 2:
        return 2
    else:
        # x = Staircase(N - 1)  # If I have taken 1 step
        # y = Staircase(N - 2)  # If I have taken 2 steps
        # z = Staircase(N - 3)  # If I have taken 3 steps
        return Staircase(N - 1) + Staircase(N - 2) + Staircase(N - 3)


num = int(input())
#res = Staircase(int(num))
print(Staircase(num))
# Example:
# N=1 -> 1 : 1 way
# N=2 -> 1,1 or 2 : 2 ways
# N=3 -> 1,1,1 or 1,2 or 2,1 or 3 : 4 ways
