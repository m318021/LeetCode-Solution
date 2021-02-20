# 191. Number of 1 Bits - Easy
# https://leetcode.com/problems/number-of-1-bits/


class Solution:
    def hammingWeight(self, n: int) -> int:
        res=0
        while n:
            res+=(n&1)
            n>>=1
        return res




if __name__ == '__main__':
    n = 11
    input = '{:032b}'.format(n)
    result = Solution().hammingWeight( n )
    print("Input: {}\nOutput: {}\nExpect: True".format(input, result))