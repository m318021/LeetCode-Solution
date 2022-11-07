from utility.test_lib import process_tree_node

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        newTree = TreeNode()
        head = TreeNode(0, right=newTree)

        # DFS
        def dfs(root, newTree):
            if root is not None:
                # Left
                newTree = dfs(root.left, newTree)

                # Step
                newTree.right = TreeNode(root.val)
                newTree = newTree.right

                # Right
                newTree = dfs(root.right, newTree)

            return newTree

        # Result
        newTree = dfs(root, newTree)

        return head.right.right


if __name__ == '__main__':
    root = [5,3,6,2,4,None,8,1,None,None,None,7,9]
    tree = process_tree_node().build_binary_tree(root)
    process_tree_node().print_binary_tree(tree)
    output = Solution().increasingBST(tree)
    print(str(output) + "\n")

    root = [5, 1, 7]
    tree = process_tree_node().build_binary_tree(root)
    process_tree_node().print_binary_tree(tree)
    output = Solution().increasingBST(tree)
    print(str(output) + "\n")