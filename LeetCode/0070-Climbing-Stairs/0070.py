# https://leetcode.com/problems/climbing-stairs/
# f(n) = f(n-1) + f(n-2)

class Solution:
    def climbStairs(self, n: int) -> int:

        climb = {}
        return self._climbStairs(n, climb)

    def _climbStairs(self, n, climb):
        if n == 0 or n==1:
            return 1

        if n not in climb:
            climb[n] = self._climbStairs(n-1, climb) + self._climbStairs(n-2, climb)

        return climb[n]


if __name__ == '__main__':
    n = 2
    result = Solution().climbStairs(n)
    print(result)

    print("===========================")
    n = 3
    result = Solution().climbStairs(n)
    print(result)

    for i in range(1,46):
        result = Solution().climbStairs(i)
        print("{} : {}".format(i,result))








