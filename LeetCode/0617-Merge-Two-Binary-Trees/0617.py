from utility.test_lib import process_tree_node

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1: [TreeNode], root2: [TreeNode]) -> [TreeNode]:
        if not root1 and root2:
            return root2
        if not root2 and root1:
            return root1
        if not root1 and not root2:
            return None

        new_tree = TreeNode(root1.val + root2.val)
        new_tree.left = self.mergeTrees(root1.left, root2.left)
        new_tree.right = self.mergeTrees(root1.right, root2.right)

        return new_tree


if __name__ == '__main__': 
    root1 = [1,3,2,5]
    root2 = [2,1,3,None,4,None,7]
    tree1 = process_tree_node().build_binary_tree(root1)
    tree2 = process_tree_node().build_binary_tree(root2)
    process_tree_node().print_binary_tree(tree1)
    process_tree_node().print_binary_tree(tree2)
    output = Solution().mergeTrees(tree1, tree2)
    # print("\n" + str(output) + "\n")
    process_tree_node().print_binary_tree(output)


    root1 = [1]
    root2 = [1, 2]
    tree1 = process_tree_node().build_binary_tree(root1)
    tree2 = process_tree_node().build_binary_tree(root2)
    process_tree_node().print_binary_tree(tree1)
    process_tree_node().print_binary_tree(tree2)
    output = Solution().mergeTrees(tree1, tree2)
    # print("\n" + str(output) + "\n")
    process_tree_node().print_binary_tree(output)


