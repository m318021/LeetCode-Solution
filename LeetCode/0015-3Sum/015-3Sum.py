# 1. 3Sum - Medium
# https://leetcode.com/problems/3sum/

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

    	nums.sort()
    	length = len(nums)
    	result_list = []

    	for i in range(length-2):

    		if nums[i] > 0:
    			break
    		if i > 0 and nums[i] == nums[i - 1]:
    			continue
    		j, k = i+1, length-1

    		while j < k:
    			result = nums[i] + nums[j] + nums[k]
    			if result < 0:
    				j += 1
    			elif result > 0:
    				k -= 1
    			else:
    				result_list.append([nums[i], nums[j], nums[k]])
    				while j + 1 < k and nums[j] == nums[j + 1]:
    					j += 1
    				while k - 1 > j and nums[k] == nums[k - 1]:
    					k -= 1
    				j += 1
    				k -= 1

    	return result_list



if __name__ == '__main__':

    nums = [ -1, 0, 1, 2, -1, -4 ]
    result = Solution().threeSum(nums)
    
    print(result)