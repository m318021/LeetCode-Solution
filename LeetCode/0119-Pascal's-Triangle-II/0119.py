from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [[1]*(i+1) for i in range(rowIndex+1)]
        for i in range(rowIndex+1):
            for j in range(1, i):
                result[i][j] = result[i-1][j-1] + result[i-1][j]
        return result[rowIndex]





        return []
if __name__ == '__main__': 
    rowIndex = 3
    output = Solution().getRow(rowIndex)
    print(output)

    rowIndex = 0
    output = Solution().getRow(rowIndex)
    print(output)

    rowIndex = 1
    output = Solution().getRow(rowIndex)