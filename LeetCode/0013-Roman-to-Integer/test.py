from typing import List
from roman_to_integer import Solution

def func_test(s, expect):
    result = Solution().romanToInt(s)
    print("Input: s = {} \nOutput = {}\n".format(s, result))
    assert result == expect

if __name__ == '__main__':

    list_input = [
        ["III", 3],
        ["IV", 4],
        ["IX", 9],
        ["LVIII", 58],
        ["MCMXCIV", 1994]
    ]

    for input in list_input:
        func_test(input[0], input[1])
