class Soultion (object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        length = len(prices)
        curren_min = prices[0]
        Profitfoward = [0]*length
        for price in range(1, length):
            Profitfoward[price] = max(Profitfoward[price-1], prices[price]-curren_min)
            curren_min = min(prices[price], curren_min)
        curren_max = prices[-1]
        ProfitBack = [0]*length
        for price in range(length-2,-1,-1):
            ProfitBack[price] =max(ProfitBack[price+1], curren_max-prices[price])
            curren_max = max(prices[price], curren_max)
        Profit = 0
        for i in range(length):
            Profit = max(Profit, Profitfoward[i]+ProfitBack[i])
        return Profit
print(Soultion().maxProfit([4,4,6,1,1,4,2,5]))
