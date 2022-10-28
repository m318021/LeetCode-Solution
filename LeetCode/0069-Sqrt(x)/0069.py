# https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        # i = 0
        # while (i * i <= x):
        #     i = i + 1
        #
        # return i - 1

        n = x
        while n * n > x:
            n = (n + x // n) // 2
        return n


if __name__ == '__main__':
    x = 4
    result = Solution().mySqrt(x)
    print(result)

    x = 8
    result = Solution().mySqrt(x)
    print(result)

    x = 169
    result = Solution().mySqrt(x)
    print(result)