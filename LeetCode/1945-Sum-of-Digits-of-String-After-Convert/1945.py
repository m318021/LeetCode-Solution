# https://leetcode.com/problems/length-of-last-word/

class Solution:
    def getLucky(self, s: str, k: int) -> int:


        test_string = ""
        for char in s:
            test_string += str(ord(char)-96)

        result = 0
        for i in range(k):
            sum = 0
            for j in test_string:
                sum = sum+int(j)
            str_sum = str(sum)
            test_string=str_sum


        result = int(sum)


        return result

if __name__ == '__main__':
    s = "iiii"
    k = 1
    result = Solution().getLucky(s, k)
    print(result)
    print("======")
    s = "leetcode"
    k = 2
    result = Solution().getLucky(s, k)
    print(result)
    print("======")
    s = "zbax"
    k = 2
    result = Solution().getLucky(s, k)
    print(result)
    print("======")
    # s= "Today is a nice day"
    # result = Solution().getLucky(s, k)
    # print(result)