def GeometricSum(k):
    if k == 0:
        return 1
    else:
        return (1 / (2 ** k)) + GeometricSum(k - 1)

lastNum = 3
print("{0:.5f}".format(GeometricSum(lastNum)))
