from typing import List
from grumpy_bookstore_owner import Solution

def func_test(customers, grumpy, x, output):

    result = Solution().maxSatisfied(customers, grumpy, x)
    print( "customers = {}, grumpy = {}, X = {}\nOutput = {}".format(customers, grumpy, x, result) )
    assert result == output

if __name__ == '__main__':

    # input item:[ customers, grumpy, x, output]
    list_input = [
        [ [1, 0, 1, 2, 1, 1, 7, 5], [0, 1, 0, 1, 0, 1, 0, 1], 3, 16],
        [[1, 0, 1, 2, 1, 1, 7, 8], [0, 1, 0, 1, 0, 1, 0, 1], 4, 19]
    ]

    for input in list_input:
        func_test(input[0], input[1], input[2], input[3])
        print("")