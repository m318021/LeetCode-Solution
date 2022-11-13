from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        result = [[1]*(i+1) for i in range(numRows)]
        print(result)
        for i in range(numRows):
            for j in range(1, i):
                print("i={}, j={}".format(i,j))
                result[i][j] = result[i-1][j-1] + result[i-1][j]
                print(result[i][j])


        return result

if __name__ == '__main__': 
    numRows = 5
    output = Solution().generate(numRows)
    print(output)

    numRows = 1
    output = Solution().generate(numRows)
    print(output)