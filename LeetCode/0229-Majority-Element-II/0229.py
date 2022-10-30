from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:


        if not nums:
            return []

        cur1, tag1 = 0, 0
        cur2, tag2 = 0, 0

        for num in nums:
            if num == tag1:
                cur1 += 1
            elif num == tag2:
                cur2 += 1
            elif cur1 == 0:
                tag1 = num
                cur1 = 1
            elif cur2 ==0:
                tag2 = num
                cur2 = 1
            else:
                cur1 -=1
                cur2 -= 1

        return [num for num in set([tag1, tag2]) \
                if nums.count(num) > len(nums) // 3]

if __name__ == '__main__':
    nums = [3, 2, 3]
    output = Solution().majorityElement(nums)
    print(output)

    nums = [1]
    output = Solution().majorityElement(nums)
    print(output)

    nums = [1,2]
    output = Solution().majorityElement(nums)
    print(output)

    nums = [2,1,1,3,1,4,5,6]
    output = Solution().majorityElement(nums)
    print(output)