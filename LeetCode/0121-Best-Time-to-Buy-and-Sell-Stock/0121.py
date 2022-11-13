import collections
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float('inf')
        result = 0


        for price in prices:
            print(price)
            print(buy)
            print(result)
            print("")
            if buy > price:
                buy = price

            if result < price - buy:
                result = price - buy
        print("--------")
        return result


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    output = Solution().maxProfit(prices)
    print(output)

    prices = [7, 6, 4, 3, 1]
    output = Solution().maxProfit(prices)
    print(output)