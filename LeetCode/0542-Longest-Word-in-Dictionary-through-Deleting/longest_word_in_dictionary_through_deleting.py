# 524. Longest Word in Dictionary through Deleting - Medium
# https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/

from typing import List
import collections

class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:

        ans = []
        dmap = collections.defaultdict(list)

        for w in d:
            dmap[w[0]].append((0, w))

        print(dmap)

        for c in s:
            wlist = dmap[c]
            del dmap[c]
            # print(dmap)
            # print(wlist)
            for i, w in wlist:
                if i + 1 == len(w):
                    ans.append(w)
                else:
                    dmap[w[i + 1]].append((i + 1, w))

        if not ans: return ''
        maxl = len(max(ans, key = len))

        return min(w for w in ans if len(w) == maxl)

        # result = ""
        # list_d = sorted(d,key = lambda i:len(i),reverse=True)
        #
        # for dict in list_d:
        #     temp = ""
        #     first = 0
        #
        #     for ch in s:
        #         if len(temp) < len(dict):
        #             if ch == dict[first]:
        #                 temp += ch
        #                 first = first + 1
        #
        #         if temp == dict and len(dict)>=len(result):
        #             if len(dict) > len(result):
        #                 result = temp
        #             elif len(temp) == len(result):
        #                 if temp[0] < result[0]:
        #                     result = temp
        #             else:
        #                 return result
        #
        # return result






