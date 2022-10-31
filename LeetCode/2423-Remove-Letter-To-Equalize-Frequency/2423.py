import collections
from typing import List

class Solution:
    def equalFrequency(self, word: str) -> bool:

        for i in range(len(word)):
            d = collections.Counter(word)
            d[word[i]] -= 1
            if d[word[i]] == 0:
                del d[word[i]]

            if len(set(d.values())) == 1:
                return True

        return False



if __name__ == '__main__': 
    word = "abcc"
    output = Solution().equalFrequency(word)
    print(output)

    word = "aazz"
    output = Solution().equalFrequency(word)
    print(output)

    word = "cccaa"
    output = Solution().equalFrequency(word)
    print(output)

    word = "bac"
    output = Solution().equalFrequency(word)
    print(output)


