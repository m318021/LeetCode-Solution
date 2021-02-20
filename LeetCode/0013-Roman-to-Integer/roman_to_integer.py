# 0013. Roman to Ingeger - Easy
# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:

        dict_roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        value = 0
        for i in range(len(s) - 1):
            if dict_roman[s[i]] >= dict_roman[s[i + 1]]:
                value += dict_roman[s[i]]
            else:
                dict_roman[s[i + 1]] -= dict_roman[s[i]]
        value += dict_roman[s[len(s) - 1]]

        return value

