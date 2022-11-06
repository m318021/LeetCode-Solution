from utility.test_lib import process_tree_node

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDiffInBST(self, root:[TreeNode]) -> int:
        if not root:
            return 0

        output = []
        self.inorder(root,output)
        min_diff = float('inf')
        for i in range(1, len(output)):
            min_diff = min(min_diff, output[i]-output[i-1])

        return min_diff

    def inorder(self, root, output):
        if root == None:
            return
        self.inorder(root.left, output)
        output.append(root.val)
        self.inorder(root.right, output)
        return output


if __name__ == '__main__':
    root = [4, 2, 6, 1, 3]
    tree = process_tree_node().build_binary_tree(root)
    process_tree_node().print_binary_tree(tree)
    output = Solution().minDiffInBST(tree)
    print(str(output) + "\n")

    root = [1, 0, 48, None, None, 12, 49]
    tree = process_tree_node().build_binary_tree(root)
    process_tree_node().print_binary_tree(tree)
    output = Solution().minDiffInBST(tree)
    print(str(output) + "\n")