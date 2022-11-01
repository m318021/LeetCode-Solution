from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set_1 = set(nums1)
        set_2 = set(nums2)
        result = []
        for key in set_1:
            if key in set_2:
                result.append(key)

        return result


if __name__ == '__main__':
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    output = Solution().intersection(nums1, nums2)
    print(output)

    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    output = Solution().intersection(nums1, nums2)
    print(output)

    nums1 = [1]
    nums2 = [1,2]
    output = Solution().intersection(nums1, nums2)
    print(output)
