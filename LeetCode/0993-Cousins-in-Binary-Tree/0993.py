import collections
from typing import List
from utility.test_lib import process_tree_node
from utility.test_lib import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isCousins(self, root: [TreeNode], x: int, y: int) -> bool:
        if not root:
            return False

        queue = collections.deque()
        queue.append((None, root))

        while queue:
            len_queue = len(queue)

            for _ in range(len_queue):
                cur = queue.popleft()
                find_x, find_y = False, False
                parent_x = None
                parent_y = None

                if x == cur[1].val:
                    parent_x = cur[0]

                    find_x = True
                if y == cur[1].val:
                    parent_y = cur[0]
                    find_y = True
                if parent_y:
                    print(parent_y.val)
                print(find_x)
                print(find_y)

                if parent_x:
                    print(parent_x.val)
                if cur[1].left != None:
                    queue.append( (cur[1],cur[1].left) )

                if cur[1].right != None:
                    queue.append( (cur[1],cur[1].right) )



        return False


if __name__ == '__main__':
    root = [1,2,3,4]
    x = 4
    y = 3

    tree = process_tree_node().build_binary_tree(root)
    process_tree_node().print_binary_tree(tree)
    output = Solution().isCousins(tree, x, y)
    print(str(output) + "\n")


    # root = [1, 2, 3, None, 4, None, 5]
    # x = 5
    # y = 4
    #
    # tree = process_tree_node().build_binary_tree(root)
    # process_tree_node().print_binary_tree(tree)
    # output = Solution().isCousins(tree, x, y)
    # print(str(output) + "\n")
    #
    # root = [1, 2, 3, None, 4]
    # x = 2
    # y = 3
    # tree = process_tree_node().build_binary_tree(root)
    # process_tree_node().print_binary_tree(tree)
    # output = Solution().isCousins(tree, x, y)
    # print(str(output) + "\n")