from typing import List

class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        return []

if __name__ == '__main__': 

    rows = 1
    cols = 2
    rCenter = 0
    cCenter = 0
    output = Solution().allCellsDistOrder(rows, cols, rCenter, cCenter)
    print(output)

    rows = 2
    cols = 2
    rCenter = 0
    cCenter = 1
    output = Solution().allCellsDistOrder(rows, cols, rCenter, cCenter)
    print(output)

    rows = 2
    cols = 3
    rCenter = 1
    cCenter = 2
    output = Solution().allCellsDistOrder(rows, cols, rCenter, cCenter)
    print(output)