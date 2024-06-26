# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         i = 0
#         profit = 0
#         smaller_val = prices[0]
#         for i in range(len(prices)):
#             cur_val = prices[i]
#             profit = max(profit, cur_val - smaller_val) # this updates the upside.
#             if smaller_val > cur_val: # this update the down side.
#                 smaller_val = cur_val
#             i += 1
#         return profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice, maxProfit  = float('inf'), 0
        for price in prices:
            if price < minPrice:
                minPrice = price
            elif price - minPrice > maxProfit:
                maxProfit = price - minPrice
        return maxProfit