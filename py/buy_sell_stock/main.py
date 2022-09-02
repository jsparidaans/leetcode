from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right, max_profit = 0, 1, 0
        while right < len(prices):
            profit = prices[right]-prices[left]
            if prices[left] < prices[right]:
                max_profit = max(profit,max_profit)
            else:
                left = right
            right += 1
        return max_profit




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution().maxProfit([7, 6, 4, 3, 1])
    print(solution)

    # See PyCharm help at https://www.jetbrains.com/help/pycharm/
