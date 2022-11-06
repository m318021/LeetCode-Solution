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
    def getMinimumDifference(self, root: [TreeNode]) -> int:
        if not root:
            return 0
        output = []
        self.inorder(root, output)
        print(output)

        min_abs = float('inf')
        for i in range(1, len(output)):
            min_abs = min(min_abs, abs(output[i] - output[i-1]))

        return min_abs

    def inorder(self, root, queue):
        if root == None:
            return

        self.inorder(root.left, queue)
        queue.append(root.val)
        self.inorder(root.right, queue)

        return queue



if __name__ == '__main__': 
    root = [4,2,6,1,3]
    tree = process_tree_node().build_binary_tree(root)
    process_tree_node().print_binary_tree(tree)
    output = Solution().getMinimumDifference(tree)
    print(str(output) + "\n")

    root = [1, 0, 48, None, None, 12, 49]
    tree = process_tree_node().build_binary_tree(root)
    process_tree_node().print_binary_tree(tree)
    output = Solution().getMinimumDifference(tree)
    print(str(output) + "\n")

    root = [236,104,701,None,227,None,911]
    tree = process_tree_node().build_binary_tree(root)
    process_tree_node().print_binary_tree(tree)
    output = Solution().getMinimumDifference(tree)
    print(str(output) + "\n")


