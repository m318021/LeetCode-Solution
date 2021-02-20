# 16. 3Sum Closest - Medium 
# https://leetcode.com/problems/3sum-closest/
from typing import List

class Solution:
    def helper(self, nums, left, target, curr, res):
        right = len(nums)-1
        print("right = {}".format(right))
        while left<right:
            curr_sum = curr+nums[left]+nums[right]
            print("left={}".format(left))
            print("curr_sum={}".format(curr_sum))
            diff = abs(curr_sum-target)
            if diff<res[0]:
                res[0] = diff
                res[1] = curr_sum
                
            if curr_sum<target: 
                left+=1
                while left<right and nums[left]==nums[left-1]: left+=1
            elif curr_sum>target:
                right-=1
                while left<right and nums[right]==nums[right+1]: right-=1
            else:
                return
            
            
                
        
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        print(nums)
        res = [float('inf'), 0]
        print(res)
        
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]: continue
            self.helper(nums, i+1, target, nums[i], res)
            if res[1]==target: return res[1]
        
        return res[1]
                    



    # def threeSumClosest(self, nums: List[int], target: int) -> int:

    #     N = len(nums)
    #     nums.sort()
    #     res = float('inf') # sum of 3 number
    #     for t in range(N):
    #         i, j = t + 1, N - 1
    #         while i < j:
    #             _sum = nums[t] + nums[i] + nums[j]
    #             if abs(_sum - target) < abs(res - target):
    #                 res = _sum
    #             if _sum > target:
    #                 j -= 1
    #             elif _sum < target:
    #                 i += 1
    #             else:
    #                 return target
    #     return res





if __name__ == '__main__':

	nums = [-1,2,1,-4] 
	target = 1

	result = Solution().threeSumClosest(nums, target)
	print("Output : {}".format(result))