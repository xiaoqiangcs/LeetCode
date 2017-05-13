class Soultion (object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        curren_min=2**31-1
        Profit = 0
        for price in prices:
            Profit = max(Profit, price-curren_min)
            curren_min = min(price, curren_min)
        return Profit
print(Soultion().maxProfit([3,2,3,1,2]))
