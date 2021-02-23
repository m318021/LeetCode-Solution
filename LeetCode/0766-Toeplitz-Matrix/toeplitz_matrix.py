# 766. Toeplitz Matrix - Easy
# https://leetcode.com/problems/toeplitz-matrix/


from typing import List
import collections

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:

        dict_map = {}

        for row in range(len(matrix)):
            row_list = matrix[row]
            for column in range(len(row_list)):
                diff = row-column
                if diff not in dict_map:
                    dict_map[diff] = row_list[column]
                else:
                    if dict_map[diff] != row_list[column]:
                        return False

        return True


