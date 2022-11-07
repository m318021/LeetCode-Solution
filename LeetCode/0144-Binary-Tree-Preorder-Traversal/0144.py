from typing import List
from utility.test_lib import process_tree_node


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: [TreeNode]) -> List[int]:
        if not root:
            return []
        result = []

        self.preorder(root, result)

        return result

    def preorder(self, root, result):
        if not root:
            return None

        result.append(root.val)

        self.preorder(root.left, result)
        self.preorder(root.right, result)

        return result



if __name__ == '__main__': 
    root = [1,None,2,3]
    tree = process_tree_node().build_binary_tree(root)
    process_tree_node().print_binary_tree(tree)
    output = Solution().preorderTraversal(tree)
    print(str(output) + "\n")

    root = []
    tree = process_tree_node().build_binary_tree(root)
    process_tree_node().print_binary_tree(tree)
    output = Solution().preorderTraversal(tree)
    print(str(output) + "\n")

    root = [1]
    tree = process_tree_node().build_binary_tree(root)
    process_tree_node().print_binary_tree(tree)
    output = Solution().preorderTraversal(tree)
    print(str(output) + "\n")