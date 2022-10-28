from typing import List

class Solution:
    def cellsInRange(self, s: str) -> List[str]:

        result = []
        for col_index in range(ord(s[0]), ord(s[3])+1):
            for row_index in range(int(s[1]), int(s[4])+1):
                temp = chr(col_index)+str(row_index)
                result.append(temp)

        return result


if __name__ == '__main__':
    s = "K1:L2"
    output = Solution().cellsInRange(s)
    print(output)

    s = "A1:F1"
    output = Solution().cellsInRange(s)
    print(output)

