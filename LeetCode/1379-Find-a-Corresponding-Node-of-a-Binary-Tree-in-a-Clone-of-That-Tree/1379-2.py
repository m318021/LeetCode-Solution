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
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not original or not cloned:
            return None

        queue = collections.deque()
        queue.append(cloned)
        tree = None
        while queue:
            node = queue.popleft()

            if node != None:
                if node.val == target.val:
                    tree = node
                    break
                else:
                    queue.append(node.left)
                    queue.append(node.right)

        return tree

if __name__ == '__main__':
    tree = [7,4,3,None,None,6,19]
    target = TreeNode(3)
    tree1 = process_tree_node().build_binary_tree(tree)
    tree2 = process_tree_node().build_binary_tree(tree)
    process_tree_node().print_binary_tree(tree1)
    output = Solution().getTargetCopy(tree1, tree2, target)
    print(str(output) + "\n")

    tree = [7]
    target = TreeNode(7)
    tree1 = process_tree_node().build_binary_tree(tree)
    tree2 = process_tree_node().build_binary_tree(tree)
    process_tree_node().print_binary_tree(tree1)
    output = Solution().getTargetCopy(tree1, tree2, target)
    print(str(output) + "\n")

    tree = [8,None,6,None,5,None,4,None,3,None,2,None,1]
    target = TreeNode(4)
    tree1 = process_tree_node().build_binary_tree(tree)
    tree2 = process_tree_node().build_binary_tree(tree)
    process_tree_node().print_binary_tree(tree1)
    output = Solution().getTargetCopy(tree1, tree2, target)
    print(str(output) + "\n")