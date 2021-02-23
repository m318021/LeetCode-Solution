# 1052. Grumpy Bookstore Owner - Medium
# https://leetcode.com/problems/grumpy-bookstore-owner/
# https://leetcode-cn.com/problems/grumpy-bookstore-owner/

from typing import List

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:

        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type X: int
        :rtype: int
        """
        res = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                res += customers[i]
                customers[i] = 0
        max_count = 0
        val = 0
        for i in range(len(customers)):
            if i < X:
                val += customers[i]
                continue
            max_count = max(val,max_count)
            val -= customers[i-X]
            val += customers[i]
        max_count = max(val, max_count)
        #print customers
        #print res
        return res + max_count




if __name__ == '__main__':
    customers = [1, 0, 1, 2, 1, 1, 7, 5]
    grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
    x = 3

    result = Solution().maxSatisfied(customers, grumpy, x)
    print( "customers = {}, grumpy = {}, X = {}\nOutput = {}".format(customers, grumpy, x, result) )





