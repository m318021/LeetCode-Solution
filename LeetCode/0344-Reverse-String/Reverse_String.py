# 344 Reverse String- Easy 
# https://leetcode.com/problems/reverse-string/

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s) -1
        while i<j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1





if __name__ == '__main__':

    s1 = ["h","e","l","l","o"]
    print("Input = {}".format(s1))
    Solution().reverseString(s1)
    s2 = ["H","a","n","n","a","h"]
    print("Input = {}".format(s2))
    Solution().reverseString(s1)
    