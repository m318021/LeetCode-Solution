# https://leetcode.com/problems/ugly-number/

class Solution:
    def isUgly(self, n: int) -> bool:

        if  n<=0:
            return False

        for i in [2,3,5]:
            while n % i == 0:
                n = n/i

        return True if n == 1 else False



if __name__ == '__main__':
    n = 6
    result = Solution().isUgly(n)
    print(result)

    n = 1
    result = Solution().isUgly(n)
    print(result)

    n = 14
    result = Solution().isUgly(n)
    print(result)