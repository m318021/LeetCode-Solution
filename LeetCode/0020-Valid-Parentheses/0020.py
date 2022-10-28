# 20. Valid Parentheses - Easy
# https://leetcode.com/problems/valid-parentheses/

from typing import List

class Solution:
    def isValid(self, s: str) -> bool:

    
        if len(s)%2 == 1:
            return False

        pop_list = []

        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                pop_list.append(s[i])
            else:
                if not pop_list:
                    return False
                else:
                    check = pop_list.pop()
                    if s[i] == ')' and check != '(':
                        return False
                    elif s[i] == ']' and check != '[':
                        return False
                    elif s[i] == '}' and check != '{':
                        return False
        if not pop_list: 
            return True
        else:
            return False
            



if __name__ == '__main__':

    s = "()"
    result = Solution().isValid(s)
    print("Input: {}, Output = {}\nExpect = True\n".format(s, result))


    s = "()[]{}"
    result = Solution().isValid(s)
    print("Input: {}, Output = {}\nExpect = True\n".format(s, result))

    s = "(]"
    result = Solution().isValid(s)
    print("Input: {}, Output = {}\nExpect = False\n".format(s, result))

    s = "([)]"
    result = Solution().isValid(s)
    print("Input: {}, Output = {}\nExpect = False\n".format(s, result))

    s = "{[]}"
    result = Solution().isValid(s)
    print("Input: {}, Output = {}\nExpect = True\n".format(s, result))
