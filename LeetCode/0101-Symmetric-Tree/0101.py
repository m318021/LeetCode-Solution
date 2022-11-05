from typing import List
#BFS

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: [TreeNode]) -> bool:
        if not root:
            return True

        return self.helper(root.left, root.right)

    def helper(self, left, right):
        if left == None and right == None:
            return True
        elif left == None or right == None:
            return False
        elif left.val != right.val:
            return False
        else:
            return self.helper(left.left, right.right) and self.helper(left.right, right.left)



if __name__ == '__main__':
    root = [1,2,2,3,4,4,3]
    tree = TreeNode(root[0])
    tree.left = TreeNode(root[1])
    tree.right = TreeNode(root[2])
    tree.left.left = TreeNode(root[3])
    tree.left.right = TreeNode(root[4])
    tree.right.left = TreeNode(root[5])
    tree.right.right = TreeNode(root[6])

    output = Solution().isSymmetric(tree)
    print(output)

    root = [1, 2, 2, None, 3, None, 3]
    tree = TreeNode(root[0])
    tree.left = TreeNode(root[1])
    tree.right = TreeNode(root[2])
    tree.left.left = TreeNode(root[3])
    tree.left.right = TreeNode(root[4])
    tree.right.left = TreeNode(root[5])
    tree.right.right = TreeNode(root[6])

    output = Solution().isSymmetric(tree)
    print(output)