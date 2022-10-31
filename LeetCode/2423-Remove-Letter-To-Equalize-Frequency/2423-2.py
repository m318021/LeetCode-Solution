import collections
from typing import List

class Solution:
    def equalFrequency(self, word: str) -> bool:

        d = collections.Counter(word)
        dd = collections.Counter(d.values())

        if len(d) == 1:
            return True

        m = len(dd)
        if m == 1:
            for freq in d.values():

                return freq == 1
        if m > 2 :
             return False

        m, M = min(d.values()), max(d.values())

        if m==1 and dd[m] == 1:
            return True

        if M-m == 1 and dd[M] == 1:
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


