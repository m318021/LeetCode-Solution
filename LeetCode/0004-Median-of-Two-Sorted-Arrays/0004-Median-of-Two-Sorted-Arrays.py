# 1. Two Sum - Easy 
# https://leetcode.com/problems/two-sum/

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        nums3 = nums1 + nums2
        nums3.sort()
        length = len(nums3)//2

        return nums3[length] if len(nums3) %2 == 1 else (nums3[length] + nums3[length-1])/2
    

    """ Algorithm without sort"""
    def findMedianSortedArraysWithoutSort(self, nums1: List[int], nums2: List[int]) -> float:


        length_1, length_2 = len(nums1), len(nums2)
        
        if length_1 ==0 and length_2 == 0:
            return 0
        elif length_1 ==0 and length_2 !=0:
            new_list = nums2
        elif length_1!=0 and length_2 ==0:
            new_list = nums1
        else:
            new_list = []
            i,j = 0,0
            while i < length_1 and j<length_2:
                if nums1[i] <= nums2[j]:
                    new_list.append(nums1[i])
                    i += 1
                else:
                    new_list.append(nums2[j])
                    j += 1

            if i == length_1:
                new_list = new_list + nums2[j:]
            elif j == length_2:
                new_list = new_list + nums1[i:]

        length = len(new_list)
        return new_list[length//2] if length % 2 == 1 else (new_list[length//2-1] + new_list[length//2])/2
        




    
if __name__ == '__main__':


    result1 = Solution().findMedianSortedArrays([1,3], [2])
    print("input nums1 = [1,3], nums2 = [2], \nOutput = {:.5f}\n".format(float(result1)))
    result2 = Solution().findMedianSortedArrays([1,2], [3,4])
    print("input nums1 = [1,2], nums2 = [3,4], \nOutput = {:.5f}\n".format(float(result2)))
    result3 = Solution().findMedianSortedArrays([], [2,3])
    print("input nums1 = [], nums2 = [2,3], \nOutput = {:.5f}\n".format(float(result3)))
    result4 = Solution().findMedianSortedArrays([0,0],[0,0])
    print("input nums1 = [0,0], nums2 = [0,0], \nOutput = {:.5f}\n".format(float(result4)))
    result5 = Solution().findMedianSortedArrays([],[1,2,3,4])
    print("input nums1 = [], nums2 = [1,2,3,4], \nOutput = {:.5f}\n".format(float(result5)))