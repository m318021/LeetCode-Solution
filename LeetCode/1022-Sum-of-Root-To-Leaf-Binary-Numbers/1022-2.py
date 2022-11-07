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

        queue = collections.deque()
        queue.append(("", root))
        result = []
        while queue:
            node = queue.popleft()
            binary = node[0]
            if node[1]:
                binary += str(node[1].val)
                queue.append( (binary, node[1].left) )
                queue.append( (binary, node[1].right) )
                if not node[1].left and not node[1].right:
                    result.append(binary)

        sum = 0
        for binary in result:
            for i in range(len(binary)):
                sum += int(binary[i]) * pow(2, len(binary)-i-1)

        return sum


if __name__ == '__main__':
    root = [1, 0, 1, 0, 1, 0, 1]
    tree = process_tree_node().build_binary_tree(root)
    process_tree_node().print_binary_tree(tree)
    output = Solution().sumRootToLeaf(tree)
    print(str(output) + "\n")