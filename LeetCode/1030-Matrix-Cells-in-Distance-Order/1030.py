from typing import List

class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:

        all_cells = []
        map = {}
        shortest, longest = rows*cols,-1
        for i in range(rows):
            for j in range(cols):

                if abs(i-rCenter)+abs(j-cCenter) not in map:
                    map[abs(i-rCenter)+abs(j-cCenter)] = []

                map[abs(i - rCenter) + abs(j - cCenter)].append([i, j])
                if abs(i - rCenter) + abs(j - cCenter) < shortest:
                    shortest = abs(i - rCenter) + abs(j - cCenter)
                if abs(i - rCenter) + abs(j - cCenter) > longest:
                    longest = abs(i - rCenter) + abs(j - cCenter)

        result = []
        for i in range(shortest, longest+1):
            for item in map[i]:
                # print("AAAA:{}".format(item))
                result.append(item)

        return result

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