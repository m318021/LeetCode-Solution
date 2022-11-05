from typing import List
# from utility.test_lib import process_tree_node as list_lib
from utility.test_lib import process_tree_node as tree_lib

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        self.preorder(p, [])
        self.preorder(q, [])

        return self.preorder(p, []) == self.preorder(q, [])

    def preorder(self, root, preorder_list):
        if root == None:
            preorder_list.append(-1)
            return
        preorder_list.append(root.val)
        self.preorder(root.left, preorder_list)
        self.preorder(root.right, preorder_list)

        return preorder_list

if __name__ == '__main__': 
    p = [1,2,3]
    q = [1,2,3]
    node_p_1 = tree_lib().makeTreeNode(nums=p)
    node_q_1 = tree_lib().makeTreeNode(nums=q)
    # node_p_1 = TreeNode(p[0])
    # node_p_2 = TreeNode(p[1])
    # node_p_3 = TreeNode(p[2])
    #
    # node_p_1.left = node_p_2
    # node_p_1.right = node_p_3
    #
    # node_q_1 = TreeNode(q[0])
    # node_q_2 = TreeNode(q[1])
    # node_q_3 = TreeNode(q[2])
    #
    # node_q_1.left = node_q_2
    # node_q_1.right = node_q_3

    output = Solution().isSameTree(node_p_1,node_q_1)
    print(output)

    p = [1, 2]
    q = [1, None, 2]

    node_p_1 = tree_lib().makeTreeNode(nums=p)
    node_q_1 = tree_lib().makeTreeNode(nums=q)

    # node_p_1 = TreeNode(p[0])
    # node_p_2 = TreeNode(p[1])
    #
    #
    # node_p_1.left = node_p_2
    #
    #
    # node_q_1 = TreeNode(q[0])
    # node_q_2 = TreeNode(q[1])
    # node_q_3 = TreeNode(q[2])
    #
    # node_q_1.left = node_q_2
    # node_q_1.right = node_q_3
    output = Solution().isSameTree(node_p_1,node_q_1)
    print(output)

    #
    p = [1, 2, 1]
    q = [1, 1, 2]
    # node_p_1 = TreeNode(p[0])
    # node_p_2 = TreeNode(p[1])
    # node_p_3 = TreeNode(p[2])
    #
    # node_p_1.left = node_p_2
    # node_p_1.right = node_p_3
    #
    # node_q_1 = TreeNode(q[0])
    # node_q_2 = TreeNode(q[1])
    # node_q_3 = TreeNode(q[2])
    #
    # node_q_1.left = node_q_2
    # node_q_1.right = node_q_3
    node_p_1 = tree_lib().makeTreeNode(nums=p)
    node_q_1 = tree_lib().makeTreeNode(nums=q)

    output = Solution().isSameTree(node_p_1,node_q_1)
    print(output)