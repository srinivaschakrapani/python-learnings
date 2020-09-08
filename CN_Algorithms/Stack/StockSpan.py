'''
The span si of a stock’s price on a certain day i is the minimum
number of consecutive days (up to the current day) the price of the
stock has been less than its price on that ith day. If for a
particular day, if no stock price is greater then just count the
number of days till 0th day including current day. For eg. if given
price array is {3, 6, 8, 1, 2}, span for 4th day (which has price 2)
is 2 because minimum count of consecutive days (including 4th day
itself) from current day which has price less than 4th day is 2 (i.e.
day 3 & 4). Similarly, span for 2nd day is 3 because no stock price in
left is greater than 2nd day's price. So count is 3 till 0th day.
Given an input array with all stock prices, you need to return the
array with corresponding spans of each day. Note : Try doing it in
O(n).
'''

def stockSpan(price,n):
    ss = []
    res = []
    k = 0
    for i in range(n):
        if len(ss) == 0:
            ss.append(i)
            res.append(1)
        else:
            if price[i] > price[ss[-1]]:
                while len(ss) != 0:
                    t = ss[-1]
                    if price[i] > price[t]:
                        ss.pop()
                        continue
                    else:
                        res.append(i-t)
                        ss.append(i)
                        break
                else:
                    ss.append(i)
                    res.append(i + 1)
            else:
                res.append(i-ss[-1])
                ss.append(i)
    return res


#### Implement Your Code Here

n = int(input())
price = [int(ele) for ele in input().split()]
spans = stockSpan(price,n)
for ele in spans:
    print(ele,end= ' ')


'''
Edge cases:
4
156 51 60 194

'''



