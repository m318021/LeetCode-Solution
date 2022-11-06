from typing import List
import collections
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0

        max_level = 0
        queue = collections.deque()
        queue.append(root)

        while queue:

            for _ in range(len(queue)):
                node = queue.popleft()
                for child in node.children:
                    queue.append(child)
            max_level += 1

        return max_level


if __name__ == '__main__':
    root = [1,None,3,2,4,None,5,6]
    root = [1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9, 10, None, None, 11, None, 12, None, 13, None, None, 14]
