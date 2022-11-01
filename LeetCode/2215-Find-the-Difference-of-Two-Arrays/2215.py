from typing import List
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set_1 = set(nums1)
        set_2 = set(nums2)

        return [list(set_1 - set_2), list(set_2-set_1)]


if __name__ == '__main__':
    nums1 = [1,2,3]
    nums2 = [2,4,6]
    output = Solution().findDifference(nums1, nums2)
    print(output, "\n")

    nums1 = [1, 2, 3, 3]
    nums2 = [1, 1, 2, 2]
    output = Solution().findDifference(nums1, nums2)
    print(output, "\n")