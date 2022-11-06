import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCompleteTree(self, root: [TreeNode]) -> bool:
        if not root:
            return True

        # BFS
        queue = collections.deque()
        queue.append(root)
        is_none = False

        while queue:
            node = queue.popleft()
            if not node:
                is_none = True
                continue
            if is_none:
                return False

            queue.append(node.left)
            queue.append(node.right)

        return True



if __name__ == '__main__':
    root = [1,2,3,4,5,6]
    tree = TreeNode(root[0])
    tree.left = TreeNode(root[1])
    tree.right = TreeNode(root[2])
    tree.left.left = TreeNode(root[3])
    tree.left.right = TreeNode(root[4])
    tree.right.left = TreeNode(root[5])

    output = Solution().isCompleteTree(tree)
    print(output)



    root = [1, 2, 3, 4, 5, None, 7]
    tree = TreeNode(root[0])
    tree.left = TreeNode(root[1])
    tree.right = TreeNode(root[2])
    tree.left.left = TreeNode(root[3])
    tree.left.right = TreeNode(root[4])
    tree.right.left = TreeNode(root[5])
    tree.right.right = TreeNode(root[6])

    output = Solution().isCompleteTree(tree)
    print(output)