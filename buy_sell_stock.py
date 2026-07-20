
prices=[7,1,5,3,6,4]

def maxProfit(prices):
    l = 0
    maxP = 0

    for r in range(1, len(prices)):
        if prices[r] > prices[l]:
            maxP = max(maxP, prices[r] - prices[l])
        else:
            l = r

    return maxP
print(maxProfit(prices))