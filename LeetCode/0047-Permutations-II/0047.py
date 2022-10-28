from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

    	ans = [[]]

    	for i in nums:
    		print("i = {}".format(i))
    		rep_ans = []
    		print("ans = {}".format(ans))
    		for j in ans:
    			for m in range(len(j)+1):
    				rep_ans.append(j[:m]+[i]+j[m:])
    				if (m<len(j) and j[m] == i): break
    		ans = rep_ans


    	return ans

if __name__ == '__main__':


    nums = [ 1, 1, 2 ]

    result = Solution().permute(nums)
    print("Input = {}\nOutput = {}\n".format(nums, result))

    nums = [ 1, 2, 3 ]

    result = Solution().permute(nums)
    print("Input = {}\nOutput = {}\n".format(nums, result))


