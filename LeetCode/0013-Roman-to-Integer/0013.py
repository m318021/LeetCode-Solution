from typing import List

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_num = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        result = 0

        pre = 0
        for char in s:
            temp = roman_num[char]

            if pre < temp:
                result += temp - 2*pre
            else:
                result += temp
            pre = temp

        return result






if __name__ == '__main__':

    s = "III"
    output = Solution().romanToInt(s)
    print(output)

    s = "LVIII"
    output = Solution().romanToInt(s)
    print(output)

    s = "MCMXCIV"
    output = Solution().romanToInt(s)
    print(output)