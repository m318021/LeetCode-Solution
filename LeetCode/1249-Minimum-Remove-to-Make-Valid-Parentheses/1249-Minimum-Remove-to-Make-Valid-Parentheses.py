# 1249. Minimum Remove to Make Valid Parentheses - Medium
# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        temp = []
        count = 0
        for i in range(len(s)):
            if s[i] == "(":
                temp.append(i)
                count = count + 1
            elif s[i] == ")":
                if count > 0:
                    temp.pop()
                    count = count - 1
                else:
                    temp.append(i)

        result = list(s)
        for index in temp:
            result[index] = ""

        return "".join(result)


if __name__ == '__main__':

    s = "lee(t(c)o)de)"
    result = Solution().minRemoveToMakeValid( s )
    print("Input: {}\nOutput: {}\n".format(s, result))

    s = "a)b(c)d"
    result = Solution().minRemoveToMakeValid( s )
    print("Input: {}\nOutput: {}\n".format(s, result))

    s = "))(("
    result = Solution().minRemoveToMakeValid( s )
    print("Input: {}\nOutput: {}\n".format(s, result))

    s = "(a(b(c)d)"
    result = Solution().minRemoveToMakeValid( s )
    print("Input: {}\nOutput: {}\n".format(s, result))

    s = "())()((("
    result = Solution().minRemoveToMakeValid(s)
    print("Input: {}\nOutput: {}\n".format(s, result))
