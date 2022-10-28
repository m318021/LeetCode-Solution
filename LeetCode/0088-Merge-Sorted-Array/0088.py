from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m, m+n):
            nums1[i] = nums2[i-m]

        for j in range(n+m-1):
            for k in range(j+1, n+m):
                if nums1[j] > nums1[k]:
                    temp = nums1[j]
                    nums1[j] = nums1[k]
                    nums1[k] = temp

if __name__ == '__main__':
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    Solution().merge(nums1, m, nums2, n)


    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    Solution().merge(nums1, m, nums2, n)


    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    Solution().merge(nums1, m, nums2, n)

