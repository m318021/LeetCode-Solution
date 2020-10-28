# 1. Two Sum - Easy 
# https://leetcode.com/problems/two-sum/

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dict_map = {}
        
        for i in range(len(nums)):
            value = target - nums[i] 
            if value in dict_map:
                return [dict_map[value], i]
            else:
                dict_map[nums[i]] = i


if __name__ == '__main__':

    nums = [ 2, 7, 11, 15 ]
    target = 9
    result = Solution().twoSum(nums, target)
    
    print(result)