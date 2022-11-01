from typing import List

class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:

        count = 0
        for word in words:
            sub_words = s.split(word)
            if len(sub_words) > 1 and sub_words[0] == "":
                count = count + 1

        return count


if __name__ == '__main__':
    words = ["a","b","c","ab","bc","abc"]
    s = "abc"
    output = Solution().countPrefixes(words, s)
    print(output, "\n")

    words = ["a", "a"]
    s = "aa"
    output = Solution().countPrefixes(words, s)
    print(output, "\n")