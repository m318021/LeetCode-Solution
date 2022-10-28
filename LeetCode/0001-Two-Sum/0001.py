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

    result1 = Solution().twoSum([2,7,11,15], 9)
    print("Input: nums = [2,7,11,15], target = 9\nOutput = {}\n".format(result1))

    result2 = Solution().twoSum([3,2,4], 6)
    print("Input: nums = [3,2,4], target = 6\nOutput = {}\n".format(result2))