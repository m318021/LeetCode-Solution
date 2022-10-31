import collections
from typing import List

class Solution:
    def minDeletions(self, s: str) -> int:
        count_list = collections.Counter(s)
        num_list = list(sorted(count_list.values(), reverse=True))
        print(num_list)
        result = 0

        cur = num_list[0]
        for i in range(1, len(num_list)):
            print("num_list[{}]={}".format(i, num_list[i]))
            if num_list[i] >= cur:
                if cur > 0:
                    result += (num_list[i] - (cur - 1))
                    cur -= 1
                else:
                    result += num_list[i]
            else:
                cur = num_list[i]

        return result

if __name__ == '__main__':
    s = "aab"
    output = Solution().minDeletions(s)
    print(output)

    s = "aaabbbcc"
    output = Solution().minDeletions(s)
    print(output)

    s = "ceabaacb"
    output = Solution().minDeletions(s)
    print(output)

    s = "aa"
    output = Solution().minDeletions(s)
    print(output)

    s = "accdcdadddbaadbc"
    output = Solution().minDeletions(s)
    print(output)