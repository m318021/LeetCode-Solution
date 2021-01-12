# 55.  Jump Game - Medium
# https://leetcode.com/problems/jump-game/
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:


       step = nums[0]

       for i in range(1, len(nums)):

           if step > 0:

                step -= 1#默认向前走一步，即从i走到i+1,剩余步数减1

                step = max(step, nums[i])#将此位置步数与step作比较，最大值当做step

           else:

                return False

       return True




if __name__ == '__main__':
	
	nums = [2,3,1,1,4]
	result = Solution().canJump(nums)
	print("Input: nums = {}\nOutput = {}\n".format(nums, result))

	nums = [3,2,1,0,4]
	result = Solution().canJump(nums)
	print("Input: nums = {}\nOutput = {}\n".format(nums, result))

	nums = [1,3,1,1,1]
	result = Solution().canJump(nums)
	print("Input: nums = {}\nOutput = {}\n".format(nums, result))