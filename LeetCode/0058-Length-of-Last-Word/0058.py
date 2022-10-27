# https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # sub_string = s.split(" ")
        # for i in range(len(sub_string)-1,-1,-1):
        #     if sub_string[i] != "":
        #         return len(sub_string[i])

        # find = False
        # count = 0
        # index = len(s)-1
        # while(index>-1):
        #     if s[index] != " ":
        #         find = True
        #
        #     if find == True:
        #         if s[index] != " ":
        #             count = count + 1
        #         else:
        #             break
        #     index = index-1
        #
        # return count

        N = len(s)
        left, right = 0, N-1
        while right >=0 and s[right] == " ":
            right -=1
        left = right
        while left >=0 and s[left] !=" ":
            left-=1

        return right-left


if __name__ == '__main__':
    s = "Hello World"
    result = Solution().lengthOfLastWord(s)
    print(result)

    s = "   fly me   to   the moon  "
    result = Solution().lengthOfLastWord(s)
    print(result)
    s = "luffy is still joyboy"
    result = Solution().lengthOfLastWord(s)
    print(result)

    s= "Today is a nice day"
    result = Solution().lengthOfLastWord(s)
    print(result)