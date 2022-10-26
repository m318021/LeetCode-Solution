# reverse, add
from typing import List
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:


        num1 = num1[::-1]
        num2 = num2[::-1]

        long = num1 if len(num1) >= len(num2) else num2
        short = num1 if len(num1) < len(num2) else num2

        index = 0
        result = ''
        carry = 0

        while(index < len(long)):
            if index > len(short) - 1:
                short += '0'

            add = (ord(long[index]) - ord('0')) + (ord(short[index]) - ord('0')) + carry
            carry = int(add/10)
            num = add%10
            result += chr(num+ord('0'))
            index += 1


            if carry==1:
                result+='1'



        # length = len(num1) if len(num1) > len(num2) else len(num2)
        #
        # index = 0
        # result = ''
        # carry = 0
        # while(index < length):
        #     if index > len(num1)-1:
        #         num1+='0'
        #     elif index > len(num2)-1:
        #         num2+='0'
        #
        #     add = ord(num1[index]) - ord('0') + (ord(num2[index]) - ord('0')) + carry
        #     carry = int(add/10)
        #     num = add%10
        #     result += chr(num+ord('0'))
        #     index += 1
        #
        #
        # if carry==1:
        #     result+='1'

        return result[::-1]


if __name__ == '__main__':
    num1 = "11"
    num2 = "123"
    output = Solution().addStrings(num1, num2)
    print(output)

    num1 = "456"
    num2 = "77"
    output = Solution().addStrings(num1, num2)
    print(output)

    num1 = "0"
    num2 = "0"
    output = Solution().addStrings(num1, num2)
    print(output)


    num1 = "1"
    num2 = "9"
    output = Solution().addStrings(num1, num2)
    print(output)








