from typing import List
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        stream = s.split(" ")
        if len(stream) != len(pattern):
            return False

        map_p, map_s = {},{}

        for i in range(len(pattern)):
            if pattern[i] not in map_p:
                map_p[pattern[i]] = stream[i]
            elif map_p[pattern[i]] != stream[i]:
                return False

            if stream[i] not in map_s:
                map_s[stream[i]] = pattern[i]
            elif map_s[stream[i]] != pattern[i]:
                return False

        return True


if __name__ == '__main__':
    pattern = "abba"
    s = "dog cat cat dog"

    output = Solution().wordPattern(pattern, s)
    print(output)

    pattern = "abba"
    s = "dog cat cat fish"

    output = Solution().wordPattern(pattern, s)
    print(output)

    pattern = "aaaa"
    s = "dog cat cat dog"

    output = Solution().wordPattern(pattern, s)
    print(output)