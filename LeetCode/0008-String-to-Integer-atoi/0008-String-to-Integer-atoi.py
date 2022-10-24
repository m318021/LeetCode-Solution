# 8. String to Integer (atoi) - Medium 
# https://leetcode.com/problems/string-to-integer-atoi/

from typing import List

class Solution:
    def myAtoi(self, s: str) -> int:

        if not s:
            return 0
        postive = 1
        find_index = False
        num = 0

        for ch in s:
            if ch == ' ' and find_index == True:
                break
            elif ch!=' ':
                if (ch == '+' or ch == '-') and find_index == False:
                    if ch == '-':
                        postive  = -1
                    find_index = True
                else:
                    if ch >= '0' and ch <= '9':
                        num = num * 10 + ord(ch) - ord('0')
                        find_index = True
                    else:
                        break
        
        
        MAX = (2 ** 31)-1
        Min = (-2 ** 31)        
        num = num * postive 
        num = num if num <= MAX else MAX
        num = num if num >= Min else Min

 
        return num



if __name__ == '__main__':

    str1 = "42"
    result1 = Solution().myAtoi(str1)
    print("Input: str = {} \nOutput = {}\n".format(str1, result1))

    str2 = "   -42"
    result2 = Solution().myAtoi(str2)
    print("Input: str = {} \nOutput = {}\n".format(str2, result2))

    str3 = "4193 with words"
    result3 = Solution().myAtoi(str3)
    print("Input: str = {} \nOutput = {}\n".format(str3, result3))

    str4 = "words and 987"
    result4 = Solution().myAtoi(str4)
    print("Input: str = {} \nOutput = {}\n".format(str4, result4))

    str5 = "+-12"
    result5 = Solution().myAtoi(str5)
    print("Input: str = {} \nOutput = {}\n".format(str5, result5))    

    str6 = "00000-42a1234"
    result6 = Solution().myAtoi(str6)
    print("Input: str = {} \nOutput = {}\n".format(str6, result6))  


    str7 = "   +0 123"    
    result7 = Solution().myAtoi(str7)
    print("Input: str = {} \nOutput = {}\n".format(str7, result7)) 