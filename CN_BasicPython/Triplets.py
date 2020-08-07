class Triplets:
    def findSums(self, sarr, x):
        n = len(sarr)
        pair = 0
        for i in range(n):
            k = x - sarr[i]
            for j in sarr[i + 1:n]:
                if j == k:
                    pair += 1
        return pair

    def findTriplet(self, arr, n, x):
        # Your code goes here
        triplets = 0
        for i in range(n):
            match = x - arr[i]
            pairs = self.findSums(arr[i + 1:n], match)
            if pairs != 0:
                triplets = triplets + pairs
        print(triplets)


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
    n = 7
    x = 12
    tp = Triplets()
    tp.findTriplet(arr, n, x)
