


# Time:  O(n)
# Space: O(1)
#
# Say you have an array for which the ith element 
# is the price of a given stock on day i.
#
# If you were only permitted to complete at most one transaction 
# (ie, buy one and sell one share of the stock), 
# design an algorithm to find the maximum profit.

class Solution:
    def maxProfit(self, prices: 'List[int]') -> 'int':
        max_profit,min_price=0,float('inf')
        for price in prices:
            min_price=min(price, min_price)
            max_profit=max(max_profit,price-min_price)
        return max_profit
            

if __name__ == "__main__":
    result = Solution().maxProfit([3, 2, 1, 4, 2, 5, 6])
    print (result)



# Time:  O(n^2) loop runs n(n-1)/2
# Space: O(1); profit

class Solution:
    def maxProfit(self, prices: 'List[int]') -> 'int':
        profit = 0
        for i in range(len(prices)-1):
            for j in range(i,len(prices)):
                profit = max(profit,prices[j]-prices[i])
        return profit