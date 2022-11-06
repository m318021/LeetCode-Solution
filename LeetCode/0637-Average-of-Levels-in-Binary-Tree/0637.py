import collections
from typing import List
from utility.test_lib import process_tree_node

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: [TreeNode]) -> List[float]:
        if not root:
            return []
        result = []
        queue = collections.deque()
        queue.append(root)

        while queue:
            queue_len = len(queue)
            cur_sum = 0
            for _ in range(queue_len):
                cur = queue.popleft()
                cur_sum += cur.val
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

            result.append(cur_sum/queue_len)

        return result


if __name__ == '__main__': 
    root = [3,9,20,None,None,15,7]
    tree = process_tree_node().build_binary_tree(root)
    process_tree_node().print_binary_tree(tree)
    output = Solution().averageOfLevels(tree)
    print(str(output) + "\n")

    root = [3, 9, 20, 15, 7]
    tree = process_tree_node().build_binary_tree(root)
    process_tree_node().print_binary_tree(tree)
    output = Solution().averageOfLevels(tree)
    print(str(output) + "\n")