from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

    	def dfs(nums, path, length):
	    	if len(path) == length: 		
		   		result.append(path[:])
		   		
	    	else:
		   		for i in range(len(nums)):
		   			if i == 0 or nums[i] != nums[i-1]:
		   				path.append(nums[i])
		   				dfs( (nums[:i]+ nums[i+1:]), path, length)
		   				path.pop()


    	length = len(nums)
    	result = []
    	dfs(nums, [], length)

    	return result

if __name__ == '__main__':


    nums = [ 1, 2, 3 ]

    result = Solution().permute(nums)
    print("Input = {}\nOutput = {}\n".format(nums, result))


