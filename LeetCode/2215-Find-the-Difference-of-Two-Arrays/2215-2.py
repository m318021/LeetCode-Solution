from typing import List
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set_1 = set(nums1)
        set_2 = set(nums2)

        n1 = [nums1[i] for i in range(len(nums1))]
        n2 = [nums2[i] for i in range(len(nums2))]
        for i in range(len(nums1)):
            if nums1[i] in set_2:
                n1.remove(nums1[i])

        for i in range(len(nums2)):
            if nums2[i] in set_1:
                n2.remove(nums2[i])


        return [[i for i in set(n1)], [i for i in set(n2)]]


if __name__ == '__main__':
    nums1 = [1,2,3]
    nums2 = [2,4,6]
    output = Solution().findDifference(nums1, nums2)
    print(output, "\n")

    nums1 = [1, 2, 3, 3]
    nums2 = [1, 1, 2, 2]
    output = Solution().findDifference(nums1, nums2)
    print(output, "\n")