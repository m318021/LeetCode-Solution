# 1. Two Sum - Easy 
# https://leetcode.com/problems/two-sum/

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        nums3 = nums1 + nums2
        nums3.sort()
        length = len(nums3)//2

        return nums3[length] if len(nums3) %2 == 1 else (nums3[length] + nums3[length-1])/2


if __name__ == '__main__':


    result1 = Solution().findMedianSortedArrays([1,3], [2])
    print("input nums1 = [1,3], nums2 = [2], \nOutput = {:.5f}\n".format(float(result1)))
    result2 = Solution().findMedianSortedArrays([1,2], [3,4])
    print("input nums1 = [1,2], nums2 = [3,4], \nOutput = {:.5f}\n".format(float(result2)))
    result3 = Solution().findMedianSortedArrays([], [2,3])
    print("input nums1 = [], nums2 = [2,3], \nOutput = {:.5f}\n".format(float(result3)))
    result4 = Solution().findMedianSortedArrays([0,0],[0,0])
    print("input nums1 = [0,0], nums2 = [0,0], \nOutput = {:.5f}\n".format(float(result4)))