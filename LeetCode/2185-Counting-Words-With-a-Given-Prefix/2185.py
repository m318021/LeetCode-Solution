from typing import List

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:

        count = 0
        for word in words:
            sub_word = word.split(pref)
            if len(sub_word) > 1 and sub_word[0] == "":
                count = count + 1

        return count


if __name__ == '__main__':
    words = ["pay","attention","practice","attend"]
    pref = "at"
    output = Solution().prefixCount(words, pref)
    print(output,"\n")

    words = ["leetcode", "win", "loops", "success"]
    pref = "code"
    output = Solution().prefixCount(words, pref)
    print(output,"\n")


    words = ["atleetcode"]
    pref = "at"
    output = Solution().prefixCount(words, pref)
    print(output,"\n")