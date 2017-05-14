class Soultion (object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        Profit = 0
        for price in range(1,len(prices)):
            if prices[price]-prices[price-1] > 0:
                Profit+=prices[price]-prices[price-1]
        return Profit
print(Soultion().maxProfit([2,1,2,0,1]))
