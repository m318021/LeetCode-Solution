# 697 Degree of an Array - Easy
# https://leetcode.com/problems/degree-of-an-array/
# https://leetcode-cn.com/problems/degree-of-an-array/

from typing import List
import collections

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:

        if len(set(nums)) == len(nums):
            return 1

        c = collections.Counter(nums)
        max_group = [item for item in c.items() if item[1] == c.most_common(1)[0][1]]
        max_nums = [max_group[index][0] for index in range(len(max_group))]
        mac_count = max_group[0][1]

        right = len(nums) -1
        temp_left = []
        temp_right = []
        for i in max_nums:
            temp = nums.index(i)
            temp_left.append(temp)

            while right > 0:
                if nums[right] == i:
                    temp_right.append(right)
                    right = len(nums)-1
                    break
                right -= 1

        result = [temp_right[i] - temp_left[i] + 1 for i in range(len(temp_right))]

        return min(result)

        # c = collections.Counter(nums)
        # # print(c.most_common(1))
        # # print(c.most_common(1)[0])
        # # print(c.most_common(1)[0][1])
        # t = [item for item in c.items() if item[1] == c.most_common(1)[0][1]]
        # res = [t[index][0] for index in range(len(t))]
        # print("t = {}".format(t))
        # print("res = {}".format(res))
        #
        # count = t[0][1]
        # print(count)
        # right = len(nums)-1
        # temp_1 = []  #存储res中对应数的第一个下标
        # temp_2 = []  #存储对应数的最后一个下标
        # for i in res:
        #     temp = nums.index(i)
        #     print("temp = {}".format(temp))
        #     temp_1.append(temp)
        #     print("temp_1 = {}".format(temp_1))
        #     # 从右向左查找对应数值的第一个下标
        #     while right > 0:
        #         print("right = {}".format(right))
        #         if nums[right] == i:
        #             print("nums[{}] = {}".format(right,nums[right]))
        #             print("i = {}".format(i))
        #             temp_2.append(right)
        #             print("temp_2 = {}".format(temp_2))
        #             #找到后 break ,别忘记将right指向nums尾部
        #             right = len(nums) - 1
        #             break
        #         right -= 1
        #     print("")
        # final = [temp_2[k] - temp_1[k] + 1  for k in range(len(temp_1))]
        # return min(final)



if __name__ == '__main__':

    nums = [1, 2, 2, 3, 1]
    result = Solution().findShortestSubArray(nums)
    print("Input: {}\nOutput: {}\n".format(nums, result))

    nums = [1, 2, 2, 3, 1, 4, 2]
    result = Solution().findShortestSubArray(nums)
    print("Input: {}\nOutput: {}\n".format(nums, result))

    nums = [1, 5, 2, 3, 5, 4, 5, 6]
    result = Solution().findShortestSubArray(nums)
    print("Input: {}\nOutput: {}\n".format(nums, result))