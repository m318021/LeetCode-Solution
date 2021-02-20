# 242 Valid Anagram - Easy
# https://leetcode.com/problems/valid-anagram/

from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Solution - 01
        if len(s) != len(t):
            return False

        list_s = list(s)
        list_t = list(t)

        list_s.sort()
        list_t.sort()

        return list_s == list_t



if __name__ == '__main__':

    s = "anagram" 
    t = "nagaram"
    result = Solution().isAnagram(s,t)
    print("Input s = {}, t = {} \nOutput = {}\n".format(s,t,result))

    s = "rat" 
    t = "car"
    result = Solution().isAnagram(s,t)
    print("Input s = {}, t = {} \nOutput = {}\n".format(s,t,result))

    s = "aacc" 
    t = "ccac"
    result = Solution().isAnagram(s,t)
    print("Input s = {}, t = {} \nOutput = {}\n".format(s,t,result))
    
