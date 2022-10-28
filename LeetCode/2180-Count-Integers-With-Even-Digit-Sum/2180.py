# https://leetcode.com/problems/count-integers-with-even-digit-sum/

class Solution:
    def countEven(self, num: int) -> int:

        count = 0
        for i in range(1,num+1):
            str_num = str(i)
            temp = 0
            for char in str_num:
                temp += int(char)
            if temp%2==0:
                count += 1
            str_num = str(temp)
        return count


if __name__ == '__main__':
    num = 4
    result = Solution().countEven(num)
    print(result)

    num = 30
    result = Solution().countEven(num)
    print(result)