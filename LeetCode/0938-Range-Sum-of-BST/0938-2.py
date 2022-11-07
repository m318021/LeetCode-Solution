#DFS

from utility.test_lib import process_tree_node

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: [TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        def dfs(node):
            if not node: return
            if low <= node.val <= high: self.out += node.val
            if node.val > low:  dfs(node.left)
            if node.val < high: dfs(node.right)

        self.out = 0
        dfs(root)
        return self.out


if __name__ == '__main__':
    root = [10,5,15,3,7,None,18]
    low = 7
    high = 15
    tree = process_tree_node().build_binary_tree(root)
    process_tree_node().print_binary_tree(tree)
    output = Solution().rangeSumBST(tree, low, high)
    print(str(output) + "\n")


    root = [10,5,15,3,7,13,18,1,None,6]
    low = 6
    high = 10
    tree = process_tree_node().build_binary_tree(root)
    process_tree_node().print_binary_tree(tree)
    output = Solution().rangeSumBST(tree, low, high)
    print(str(output) + "\n")


    root = [10,5,15,3,7,None,18]
    low = 7
    high = 15
    tree = process_tree_node().build_binary_tree(root)
    process_tree_node().print_binary_tree(tree)
    output = Solution().rangeSumBST(tree, low, high)
    print(str(output) + "\n")