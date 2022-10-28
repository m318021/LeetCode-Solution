from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        dict_table = {}

        for i in range(len(nums)):
            if nums[i] in dict_table:
                return True
            else:
                dict_table[nums[i]] = nums[i]

        return False


if __name__ == '__main__':

    nums = [1,2,3,1]
    result = Solution().containsDuplicate( nums )
    print("Input: {}\nOutput: {}\nExpect: True".format(nums, result))

    nums=[1,2,3,4]
    result = Solution().containsDuplicate( nums )
    print("Input: {}\nOutput: {}\nExpect: False".format(nums, result))

    nums=[1,1,1,3,3,4,3,2,4,2]
    result = Solution().containsDuplicate( nums )
    print("Input: {}\nOutput: {}\nExpect: True".format(nums, result))