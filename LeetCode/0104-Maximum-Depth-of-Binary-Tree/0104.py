import collections
from typing import List
from utility.test_lib import process_tree_node

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: [TreeNode]) -> int:
        if root == None:
            return 0

        if not root.left:
            return 1 + self.maxDepth(root.right)
        elif not root.right:
            return 1 + self.maxDepth(root.left)
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


if __name__ == '__main__': 
    root = [3,9,20,None,None,15,7]
    tree = process_tree_node().build_binary_tree(root)
    process_tree_node().print_binary_tree(tree)
    output = Solution().maxDepth(tree)
    print("\n" + str(output) + "\n")

    root = [1, None, 2]
    tree = process_tree_node().build_binary_tree(root)
    process_tree_node().print_binary_tree(tree)
    output = Solution().maxDepth(tree)
    print("\n" + str(output) + "\n")