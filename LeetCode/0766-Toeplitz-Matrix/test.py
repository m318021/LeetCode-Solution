from typing import List

from toeplitz_matrix import Solution


def func_test(matrix, expect):

    result = Solution().isToeplitzMatrix(matrix)
    print("Input: matrix = {}\nOutput = {}\n".format(matrix, result))
    assert result == expect

if __name__ == '__main__':

    # input item:[s, d, output]
    list_input = [
        [ [[1,2,3,4],[5,1,2,3],[9,5,1,2]], True],
        [ [[1,2],[2,2]], False]
    ]

    for input in list_input:
        func_test(input[0], input[1])