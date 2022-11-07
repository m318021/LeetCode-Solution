from utility.test_lib import process_tree_node
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def checkTree(self, root: [TreeNode]) -> bool:
        return root.val == (root.left.val + root.right.val)


if __name__ == '__main__':
    root = [10,4,6]
    tree = process_tree_node().build_binary_tree(root)
    process_tree_node().print_binary_tree(tree)
    output = Solution().checkTree(tree)
    print(str(output) + "\n")


    root = [5, 3, 1]
    tree = process_tree_node().build_binary_tree(root)
    process_tree_node().print_binary_tree(tree)
    output = Solution().checkTree(tree)
    print(str(output) + "\n")