from utility.test_lib import process_tree_node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: [TreeNode]) -> [TreeNode]:
        if not root:
            return root

        temp = root.left
        root.left = root.right
        root.right = temp

        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)


        return root


if __name__ == '__main__':
    root = [4, 2, 7, 1, 3, 6, 9]
    tree = process_tree_node().build_binary_tree(root)
    process_tree_node().print_binary_tree(tree)
    output = Solution().invertTree(tree)
    # print("\n" + str(output) + "\n")
    process_tree_node().preorder(output)

    root = [2, 1, 3]
    tree = process_tree_node().build_binary_tree(root)
    process_tree_node().print_binary_tree(tree)
    output = Solution().invertTree(tree)
    print("\n" + str(output) + "\n")

    root = []
    tree = process_tree_node().build_binary_tree(root)
    process_tree_node().print_binary_tree(tree)
    output = Solution().invertTree(tree)
    print("\n" + str(output) + "\n")
