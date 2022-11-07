import collections
from typing import List
from utility.test_lib import process_tree_node

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumRootToLeaf(self, root: [TreeNode]) -> int:
        output = 0

        return self.traversal(root, output)


    def traversal(self, root, output):
        if not root:
            return

        output = (output << 1) + root.val

        if not root.left and not root.right:
            return output

        return self.traversal(root.left, output) + self.traversal(root.right, output)




if __name__ == '__main__':
    root = [1, 0, 1, 0, 1, 0, 1]
    tree = process_tree_node().build_binary_tree(root)
    process_tree_node().print_binary_tree(tree)
    output = Solution().sumRootToLeaf(tree)
    print(str(output) + "\n")