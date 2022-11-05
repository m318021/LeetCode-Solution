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
    def isUnivalTree(self, root: [TreeNode]) -> bool:
        queue = collections.deque()
        queue.append(root)
        cur_val = None
        while queue:
            node = queue.popleft()

            if not node:
                continue
            else:
                if not cur_val:
                    cur_val = node.val
                if node.val != cur_val:
                    return False
                queue.append(node.left)
                queue.append(node.right)

        return True


if __name__ == '__main__': 
    root = [1,1,1,1,1,None,1]
    tree = process_tree_node().build_binary_tree(root)
    process_tree_node().print_binary_tree(tree)
    output = Solution().isUnivalTree(tree)
    print(str(output) + "\n")


    root = [2, 2, 2, 5, 2]
    tree = process_tree_node().build_binary_tree(root)
    process_tree_node().print_binary_tree(tree)
    output = Solution().isUnivalTree(tree)
    print(str(output) + "\n")

    [0, 6, 0, None, None, None, 0, 0, None, 0, None, None, 0]
    tree = process_tree_node().build_binary_tree(root)
    process_tree_node().print_binary_tree(tree)
    output = Solution().isUnivalTree(tree)
    print(str(output) + "\n")