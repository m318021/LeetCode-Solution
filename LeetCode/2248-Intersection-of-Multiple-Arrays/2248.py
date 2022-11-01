from typing import List


class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        temp = set(nums[0])
        for i in range(1, len(nums)):
            temp = temp&set(nums[i])

        return sorted(list(temp))


if __name__ == '__main__':
    nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
    output = Solution().intersection(nums)
    print(output, "\n")

    nums = [[1,2,3],[4,5,6]]
    output = Solution().intersection(nums)
    print(output, "\n")

    nums = [[7,34,45,10,12,27,13],[27,21,45,10,12,13]]
    output = Solution().intersection(nums)
    print(output, "\n")