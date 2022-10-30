class Solution:
    def convertToTitle(self, columnNumber: int) -> str:

        map = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'}

        test = columnNumber
        ans = ""
        while(test>26):
            mod = test%26
            quotient = test // 26
            if mod == 0 :
                mod = 26
            else:
                quotient+=1
            ans = ans+map[mod]
            test = quotient-1
        ans += map[test]

        return ans[::-1]



if __name__ == '__main__':
    columnNumber = 1
    output = Solution().convertToTitle(columnNumber)
    print(output)

    columnNumber = 28
    output = Solution().convertToTitle(columnNumber)
    print(output)

    columnNumber = 701
    output = Solution().convertToTitle(columnNumber)
    print(output)


    columnNumber = 12345
    output = Solution().convertToTitle(columnNumber)
    print(output)

    columnNumber = 52
    output = Solution().convertToTitle(columnNumber)
    print(output)

    columnNumber = 12480
    output = Solution().convertToTitle(columnNumber)
    print(output)