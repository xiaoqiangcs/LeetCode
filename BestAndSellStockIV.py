class Soultion (object):
    def maxProfit(self, k, prices):
        if not prices:
            return 0
        length = len(prices)
        if k > length / 2:
            Profit = 0
            for price in range(1, len(prices)):
                if prices[price]-prices[price-1] > 0:
                    Profit += prices[price] - prices[price-1]
            return Profit
        Profit =[[0 for i in range(k+1)] for j in range(length+1)]
        for i in range(1,k+1):
            for j in range(1,length+1):
                for x in range(0,j+1):
                    Profit[j][i] = max(Profit[j][i],Profit[x][i-1]+self.maxsubProfit(x+1,j,prices))
        return Profit[length][k]
    def maxsubProfit(self, left, right, prices):
        if not prices:
            return 0
        prices=prices[left-1:right]
        curren_min=2**31-1
        Profit = 0
        for price in prices:
            Profit = max(Profit, price-curren_min)
            curren_min = min(price, curren_min)
        return Profit
print(Soultion().maxProfit(2,[4,4,6,1,1,4,2,5]))
