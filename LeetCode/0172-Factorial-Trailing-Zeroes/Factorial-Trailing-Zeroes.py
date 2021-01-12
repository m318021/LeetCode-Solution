# 172.Factorial Trailing Zeroes - Easy
# https://leetcode.com/problems/factorial-trailing-zeroes/

from typing import List

class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        if n < 5:
            return 0
        
        result = 0
        i = 5
        while n >= i:
            result += n//i
            i*=5
            
        return int(result)
            



if __name__ == '__main__':

    n = 3
    result = Solution().trailingZeroes(n)
    print("Input: {}, Output = {}\nExpect = 0\n".format(n, result))


    n = 5
    result = Solution().trailingZeroes(n)
    print("Input: {}, Output = {}\nExpect = 1\n".format(n, result))

    n = 1
    result = Solution().trailingZeroes(n)
    print("Input: {}, Output = {}\nExpect = 0\n".format(n, result))

