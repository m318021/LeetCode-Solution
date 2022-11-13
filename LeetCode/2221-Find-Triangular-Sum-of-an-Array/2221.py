from typing import List
class Solution:
    def triangularSum(self, nums: List[int]) -> int:

        for i in range(len(nums)-1, 0, -1):
            for j in range(i):
                nums[j] = (nums[j]+nums[j+1])%10

        return nums[0]

if __name__ == '__main__': 
    nums = [1,2,3,4,5]
    output = Solution().triangularSum(nums)
    print(output)

    nums = [5]
    output = Solution().triangularSum(nums)
    print(output)