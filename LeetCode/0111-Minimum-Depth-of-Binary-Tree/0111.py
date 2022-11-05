from typing import List
from utility.test_lib import process_tree_node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: [TreeNode]) -> int:

        if root == None:
            return 0

        if not root.left:
            return 1 + self.minDepth(root.right)
        elif not root.right:
            return 1 + self.minDepth(root.left)
        else:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))


if __name__ == '__main__':
    root = [3, 9, 20, None, None, 15, 7]
    tree = process_tree_node().build_binary_tree(root)
    # process_tree_node().print_binary_tree(tree)
    output = Solution().minDepth(tree)
    print(str(output) + "\n")

    root = [2, None, 3, None, 4, None, 5, None, 6]
    tree = TreeNode(root[0])
    tree.left = TreeNode(root[1])
    tree.right = TreeNode(root[2])
    tree.right.left = TreeNode(root[3])
    tree.right.right = TreeNode(root[4])
    tree.right.right.left = TreeNode(root[5])
    tree.right.right.right = TreeNode(root[6])
    tree.right.right.right.left = TreeNode(root[7])
    tree.right.right.right.right = TreeNode(root[8])


    # process_tree_node().print_binary_tree(tree)
    output = Solution().minDepth(tree)
    print(str(output) + "\n")

