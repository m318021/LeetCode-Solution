from typing import List
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        map = {}

        for num in nums:
            if num not in map:
                map[num] = 1
            else :
                map[num] += 1

        result, smallest = 0, -1
        for key in map:
            if key % 2 == 0:
                if map[key] > result:
                    result = map[key]
                    smallest = key
                elif map[key] == result:
                    smallest = min(key, smallest)

        return smallest

if __name__ == '__main__':
    nums = [3, 2, 3]
    output = Solution().mostFrequentEven(nums)
    print(output)

    nums = [4,4,4,9,2,4]
    output = Solution().mostFrequentEven(nums)
    print(output)

    nums = [0, 1, 2, 2, 4, 4, 1]
    output = Solution().mostFrequentEven(nums)
    print(output)

    nums = [29,47,21,41,13,37,25,7]
    output = Solution().mostFrequentEven(nums)
    print(output)

    nums = [8154,9139,8194,3346,5450,9190,133,8239,4606,8671,8412,6290]
    output = Solution().mostFrequentEven(nums)
    print(output)



