from typing import List

class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False

        reverse_value = 0
        n=x
        while n!=0:
            reverse_value = reverse_value*10 + n%10
            n = n//10

        return reverse_value == x


if __name__ == '__main__':

    input_1 = 121
    result1 = Solution().isPalindrome(input_1)
    print("Input: str = {} \nOutput = {}\nExpect = True".format(input_1, result1))

    input_2= -121
    result2 = Solution().isPalindrome(input_2)
    print("Input: str = {} \nOutput = {}\nExpect = False".format(input_2, result2))

    input_3 = 10
    result3 = Solution().isPalindrome(input_3)
    print("Input: str = {} \nOutput = {}\nExpect = False".format(input_3, result3))

    input_4 = -101
    result4 = Solution().isPalindrome(input_4)
    print("Input: str = {} \nOutput = {}\nExpect = False".format(input_4, result4))

    input_5 = 8
    result4 = Solution().isPalindrome(input_5)
    print("Input: str = {} \nOutput = {}\nExpect = True".format(input_5, result4))

    input_6 = 87899878
    result6 = Solution().isPalindrome(input_6)
    print("Input: str = {} \nOutput = {}\nExpect = True".format(input_6, result6))
