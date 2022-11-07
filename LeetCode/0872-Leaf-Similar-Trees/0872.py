from utility.test_lib import process_tree_node

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: [TreeNode], root2: [TreeNode]) -> bool:

        output1, output2 = [], []
        self.postorder(root1, output1)
        self.postorder(root2, output2)

        return output1 == output2


    def postorder(self, root, output):
        if root==None:
            return
        self.postorder(root.left, output)
        self.postorder(root.right, output)
        if not root.left and not root.right:
            output.append(root.val)

        return output



if __name__ == '__main__':
    root1 = [3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]
    root2 = [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None,9, 8]
    tree1 = process_tree_node().build_binary_tree(root1)
    tree2 = process_tree_node().build_binary_tree(root2)
    process_tree_node().print_binary_tree(tree1)
    process_tree_node().print_binary_tree(tree2)
    output = Solution().leafSimilar(tree1, tree2)
    print(str(output) + "\n")



    root1 = [1, 2, 3]
    root2 = [1, 3, 2]
    tree1 = process_tree_node().build_binary_tree(root1)
    tree2 = process_tree_node().build_binary_tree(root2)
    process_tree_node().print_binary_tree(tree1)
    process_tree_node().print_binary_tree(tree2)
    output = Solution().leafSimilar(tree1, tree2)
    print(str(output) + "\n")