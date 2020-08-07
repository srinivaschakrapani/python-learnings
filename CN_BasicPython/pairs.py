arr = [1, 3, 6, 2, 5, 4, 3, 2, 4]
n = 9
x = 7
#1,6
#3,4
#3,4
#2,5
#5,2
#4,3
#3,4

#1,2,3,4,5,6,7
#12
#1,5,6
#2,4,6
#3,4,5
#
pairs = 0
for i in range(n):
    k = arr[i]
    match = x - k
    for j in arr[i + 1:n]:
        if j == match:
            pairs += 1
print(pairs)
