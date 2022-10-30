from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        tag, cur = 0, 0
        for i in nums:
            if cur == 0:
                tag = i
            cur += 1 if tag==i else -1

        return tag

if __name__ == '__main__':
    nums = [3, 2, 3]
    output = Solution().majorityElement(nums)
    print(output)

    nums = [2, 2, 1, 1, 1, 2, 2]
    output = Solution().majorityElement(nums)
    print(output)