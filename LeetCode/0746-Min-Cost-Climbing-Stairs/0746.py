# dynamic programming


from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        n = len(cost)
        cost.append(0)
        dp = [0 for i in range(n+1)]
        dp[0], dp[1] = cost[0], cost[1]

        for i in range(2, n+1):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]

        return dp[-1]


if __name__ == '__main__':
    cost = [10, 15, 20]
    output = Solution().minCostClimbingStairs(cost)
    print(output)

    cost = [1,100,1,1,1,100,1,1,100,1]
    output = Solution().minCostClimbingStairs(cost)
    print(output)









