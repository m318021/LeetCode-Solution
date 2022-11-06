import collections
from typing import List
from utility.test_lib import process_tree_node

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: [TreeNode]) -> int:
        if not root:
            return 0
        result = 0

        if root.left != None and root.left.left == None and root.left.right == None:
            result += root.left.val

        result += self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)

        return result




if __name__ == '__main__':
    root = [3,9,20,None,None,15,7]
    tree = process_tree_node().build_binary_tree(root)
    process_tree_node().print_binary_tree(tree)
    output = Solution().sumOfLeftLeaves(tree)
    print("\n" + str(output) + "\n")

    root = []
    tree = process_tree_node().build_binary_tree(root)
    process_tree_node().print_binary_tree(tree)
    output = Solution().sumOfLeftLeaves(tree)
    print("\n" + str(output) + "\n")


    root = [1,2,3,4,5]
    tree = process_tree_node().build_binary_tree(root)
    process_tree_node().print_binary_tree(tree)
    output = Solution().sumOfLeftLeaves(tree)
    print("\n" + str(output) + "\n")


    root = [0,2,4,1,None,3,-1,5,1,None,6,None,8]
    tree = process_tree_node().build_binary_tree(root)
    process_tree_node().print_binary_tree(tree)
    output = Solution().sumOfLeftLeaves(tree)
    print("\n" + str(output) + "\n")

