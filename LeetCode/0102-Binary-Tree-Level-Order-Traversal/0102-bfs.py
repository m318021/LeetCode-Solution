from typing import List
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return []


        queue= [ root ]
        result = []
        while queue:
            temp_list = []
            for i in range(len(queue)):
                temp = queue.pop(0)
                temp_list.append(temp.val)
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
            result.append(temp_list)
        return result

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
    # n = 3
    # result = Solution().trailingZeroes(n)
    # print("Input: {}, Output = {}\nExpect = 0\n".format(n, result))


    # n = 5
    # result = Solution().trailingZeroes(n)
    # print("Input: {}, Output = {}\nExpect = 1\n".format(n, result))

    # n = 1
    # result = Solution().trailingZeroes(n)
    # print("Input: {}, Output = {}\nExpect = 0\n".format(n, result))

