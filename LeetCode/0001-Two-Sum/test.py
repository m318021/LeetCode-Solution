from two_sum import Solution

def func_test(nums, target, expect):
    result = Solution().twoSum(nums, target)
    print("Input: nums = {}, target = {}\nOutput = {}\n".format(nums, target, result))
    assert result == expect

if __name__ == '__main__':

    func_test([2,7,11,15], 9, [ 0, 1])
    func_test([3,2,4], 6, [1,2])