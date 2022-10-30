from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        map = {}

        for i in nums:
            map[i] = map.get(i, 0) + 1

        p = []
        result = []

        for key in map.items():

            heapq.heappush(p, (-key[1], -key[0]))
            if len(p) > len(map) - k:
                _, val = heapq.heappop(p)
                result.append(-val)

        return result


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    output = Solution().topKFrequent(nums, k)
    print(output)

    nums = [1]
    k = 1
    output = Solution().topKFrequent(nums, k)
    print(output)

    nums = [4,1,-1,2,-1,2,3]
    k = 2
    output = Solution().topKFrequent(nums, k)
    print(output)

    nums = [5,3,1,1,1,3,73,1]
    k = 2
    output = Solution().topKFrequent(nums, k)
    print(output)
