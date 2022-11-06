from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root:[TreeNode]) -> List[int]:
        if not root:
            return []

        output = []
        self.inorder(root, output)

        return output

    def inorder(self, root, output):
        if root == None:
            return

        self.inorder(root.left, output)
        output.append(root.val)
        self.inorder(root.right, output)

        return output


if __name__ == '__main__':
    root = [1, None, 2, 3]
    node1=TreeNode(root[0])
    node2=TreeNode(root[1])
    node3=TreeNode(root[2])
    node4=TreeNode(root[3])

    tree = node1
    node1.right = node3
    node3.left = node4


    output = Solution().inorderTraversal(tree)
    print(str(output) + "\n")

    root = []
    tree = None
    output = Solution().inorderTraversal(tree)
    print(str(output) + "\n")

    root = [1]
    tree = TreeNode(root[0])
    output = Solution().inorderTraversal(tree)
    print(str(output) + "\n")
