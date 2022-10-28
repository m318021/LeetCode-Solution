# https://leetcode.com/problems/add-digits/

class Solution:
    def addDigits(self, num: int) -> int:

        str_num = str(num)
        result = num
        while(result>9):
            temp = 0
            for i in str_num:
                temp += int(i)

            str_num=str(temp)
            result = temp

        return result

if __name__ == '__main__':
    n = 38
    result = Solution().addDigits(n)
    print(result)

    n = 0
    result = Solution().addDigits(n)
    print(result)