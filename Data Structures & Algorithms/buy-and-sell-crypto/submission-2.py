class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        bestProfit = 0

        for i in range(1, len(prices)):
            if prices[i] - minimum > bestProfit:
                bestProfit = prices[i] - minimum

            if prices[i] < minimum:
                minimum = prices[i]

        return bestProfit