# 14. Longest Common Prefix - Easy
# https://leetcode.com/problems/longest-common-prefix/

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:


        if not strs:
            return ''
        result = ''
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                    return result
            result += strs[0][i]

        return result
            



if __name__ == '__main__':

    # s = "abcabcbb"
    strs = ["flower","flow","flight"]
    result = Solution().longestCommonPrefix(strs)
    print("Input: {}, Output = {}\nExpect = {}\n".format(strs, result, "fl"))

    strs = ["dog","racecar","car"]
    result = Solution().longestCommonPrefix(strs)
    print("Input: {}, Output = {}\nExpect = {}\n".format(strs, result, ""))

    strs = ["a"]
    result = Solution().longestCommonPrefix(strs)
    print("Input: {}, Output = {}\nExpect = {}\n".format(strs, result, "a"))
