from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []
        candidates.sort()
        self.dfs(candidates, target, 0, result, [])
        return result


    def dfs(self, candidates, target, index, result, path):
        if target < 0:
            return
        elif target == 0:
            result.append(path)
            return

        for i in range(index, len(candidates)):

            if candidates[index] > target:
                return
            self.dfs(candidates, target-candidates[i], i, result, path+[candidates[i]])

if __name__ == '__main__': 
    candidates = [2,3,6,7]
    target = 7
    output = Solution().combinationSum(candidates, target)
    print(output)


    andidates = [2, 3, 5]
    target = 8
    output = Solution().combinationSum(candidates, target)
    print(output)
