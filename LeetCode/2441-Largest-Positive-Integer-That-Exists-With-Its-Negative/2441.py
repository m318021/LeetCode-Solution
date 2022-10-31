from typing import List
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        map = {}

        result = 0
        for num in nums:
            if -num not in map:
                map[num] = -num
            else:
                result = max(abs(num), result)

        return -1 if result==0 else result


if __name__ == '__main__': 

    nums = [-1, 2, -3, 3]
    print(nums)
    output = Solution().findMaxK(nums)
    print(output)

    nums = [-1, 10, 6, 7, -7, 1]
    output = Solution().findMaxK(nums)
    print(output)

    nums  = [-10,8,6,7,-2,-3]
    output = Solution().findMaxK(nums)
    print(output)