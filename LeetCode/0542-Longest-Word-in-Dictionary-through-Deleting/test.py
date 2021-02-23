from typing import List

from longest_word_in_dictionary_through_deleting import Solution


def func_test(s, d, expect):
    result = Solution().findLongestWord(s, d)
    print("Input: s = {}, d = {}\nOutput = {}\n".format(s, d, result))
    assert result == expect

if __name__ == '__main__':

    # input item:[s, d, output]
    list_input = [
        ["abpcplea", ["ale", "apple", "monkey", "plea"], "apple"],
        ["abpcplea", ["a","b","c"], "a"],
        ["bab", ["ba","ab","a","b"], "ab"]
    ]

    expect = "apple"
    for input in list_input:
        func_test(input[0], input[1], input[2])