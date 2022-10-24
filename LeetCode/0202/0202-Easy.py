# https://leetcode.com/problems/happy-number/
# hash table

class Solution:
    def isHappy(self, n: int) -> bool:
        str_n = str(n)

        result = False
        mapping_list = []
        match = False
        while (match == False):
            temp = 0
            for char in str_n:
                temp += pow(int(char), 2)
            if temp in mapping_list and temp != 1:
                match = True
            elif temp == 1:
                return True
            else:
                mapping_list.append(temp)
            str_n = str(temp)

        return result


if __name__ == '__main__':
    n = 19
    result = Solution().isHappy(n)
    print(result)

    n = 2
    result = Solution().isHappy(n)
    print(result)

    n = 7
    result = Solution().isHappy(n)
    print(result)
