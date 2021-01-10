# 0102. Binary Tree Level Order Traversal - Medium
# https://leetcode.com/problems/binary-tree-level-order-traversal/

from typing import List
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        level = 0
        node_0 = root
        result = []
        self.dfs(root, 0 , result)

        return result
    
    def dfs(self, root: TreeNode, level:int, result:List)->List:

        if root == None:
            return 
        if len(result) == level:
            result.append([])
        result[level].append(root.val)

        if root.left:
            self.dfs(root.left, level+1, result)
        if root.right:
            self.dfs(root.right, level+1, result)


    def build_tree(self, root: TreeNode, tree_list:List, index:int ) -> TreeNode:


        if index < len(tree_list):
            if (2*index) + 1 < len(tree_list):
                root.left = TreeNode( tree_list[ ( 2 * index ) + 1 ] )
                self.build_tree(root.left, tree_list, (2 * index) + 1 )
            if (2 * index + 2) < len(tree_list):
                root.right = TreeNode( tree_list[ ( 2 * index ) + 2 ] )
                self.build_tree(root.right, tree_list, ( 2 * index ) + 2 )
        else:
            return

        return root







if __name__ == '__main__':


    tree = [3,9,20,None,None,15,7]

    node_0 = TreeNode(tree[0])
    root = Solution().build_tree(node_0, tree, 0)

    result = Solution().levelOrder(root)
    print("Output = {}\n".format(result))

