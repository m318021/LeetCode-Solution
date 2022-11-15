from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        self.dfs(candidates, target, 0, result, [])

        return result

    def dfs(self, candidates, target, index, result, path):
        if target<0:
            return
        elif target==0:
            result.append(path)
            return

        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i-1]:
                continue
            self.dfs(candidates, target-candidates[i], i+1, result, path+[candidates[i]])

if __name__ == '__main__':
    candidates = [10,1,2,7,6,1,5]
    target = 8
    output = Solution().combinationSum2(candidates,target)
    print(output)

    candidates = [2,5,2,1,2]
    target = 5
    output = Solution().combinationSum2(candidates,target)
    print(output)