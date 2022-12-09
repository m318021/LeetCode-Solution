import collections
from typing import List
import math


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class process_link_list():
    def makeLinkList(self, nums: List[int]) -> ListNode:

        list_node = []
        for i in range(len(nums)):
            list_node.append(ListNode(nums[i]))

        result = list_node[0]
        for i in range(len(nums)-1):
            list_node[i].next = list_node[i+1]

        return result

    def printLinkList(self, list_node: ListNode ) :

        head = list_node

        while head != None:
            print("{} -> ".format(head.val), end='')
            head = head.next
        print("Null")


class process_tree_node():

    def build_binary_tree(self, items: list[int]) -> TreeNode:
        """Create BT from list of values."""
        n = len(items)
        if n == 0:
            return None

        def inner(index: int = 0) -> TreeNode:
            """Closure function using recursion bo build tree"""
            if n <= index or items[index] is None:
                return None

            node = TreeNode(items[index])
            node.left = inner(2 * index + 1)
            node.right = inner(2 * index + 2)
            return node

        return inner()

    def print_binary_tree(self, root):
        queue = collections.deque()
        queue.append(root)
        count = 0

        while queue:
            node = queue.popleft()
            count = count + 1
            if not node:
                print("None ",end="")
            else:
                print("{}  ".format(node.val), end="")

                queue.append(node.left)
                queue.append(node.right)

            level = math.ceil(math.log2(count))
            # print("level = {}".format(level))
            level_count = pow(2, level) - 1
            if level_count == count or count == 1:
                print("")

        print("\n")
            # print(count)
            # print(level_count)


    # def preorder(self, root):
    #     if root==None:
    #         return
    #     if root.left == None:
    #         left = "None"
    #     else:
    #         left = root.left.val
    #
    #     if root.right == None:
    #         right = "None"
    #     else:
    #         right = root.right.val
    #     print("Node = {}, left = {}, right = {}".format(root.val, left, right))
    #
    #     self.preorder(root.left)
    #     self.preorder(root.right)



if __name__ == '__main__':

    # l1 = process_link_list().makeLinkList([2,4,3])
    # l2 = process_link_list().makeLinkList([5,6,4])
    #
    #
    #
    nums = [3, 9, 20, None, None, 15, 7]
    tree = process_tree_node().build_binary_tree(items=nums)

    process_tree_node().print_binary_tree(tree)

    # #


    # nums = [2, None, 3, None, 4, None, 5, None, 6]
    # tree = process_tree_node().build_binary_tree(items=nums)
    #
    # process_tree_node().print_binary_tree(tree)

