from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # METHOD 1
        # for i in range(len(nums)):
        #     nums[i] = nums[i] * nums[i]
        #
        # for i in range(len(nums)-1):
        #     for j in range(i, len(nums)):
        #         if nums[i] > nums[j]:
        #             temp = nums[i]
        #             nums[i] = nums[j]
        #             nums[j] = temp
        #
        # return nums

        left, right = 0, len(nums)-1
        result = [0 for i in range(len(nums))]
        cur =  len(nums)-1

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[cur] = nums[left] * nums[left]
                left += 1
            else:
                result[cur] = nums[right] * nums[right]
                right -= 1

            cur -= 1

        return result

if __name__ == '__main__':
    nums = [-4,-1,0,3,10]
    output = Solution().sortedSquares(nums)
    print(output)

    nums = [-7, -3, 2, 3, 11]
    output = Solution().sortedSquares(nums)
    print(output)


