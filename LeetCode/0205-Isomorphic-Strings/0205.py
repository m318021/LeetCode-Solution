from typing import List
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map_s, map_t = {}, {}
        for i in range(len(s)):
            if s[i] not in map_s:
                map_s[s[i]] = t[i]
            elif map_s[s[i]] != t[i]:
                return False
            if t[i] not in map_t:
                map_t[t[i]] = s[i]
            elif map_t[t[i]] != s[i]:
                return False

        return True


if __name__ == '__main__':
    s = "egg"
    t = "add"
    output = Solution().isIsomorphic(s,t)
    print(output)

    s = "foo"
    t = "bar"
    output = Solution().isIsomorphic(s,t)
    print(output)

    s = "paper"
    t = "title"
    output = Solution().isIsomorphic(s,t)
    print(output)