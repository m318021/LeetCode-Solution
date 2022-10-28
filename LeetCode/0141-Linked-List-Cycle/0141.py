# https://leetcode.com/problems/linked-list-cycle/

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import List
from test_lib import process_link_list as list_lib

# class Solution:
#     def hasCycle(self, head):
#         """
#         :type head: ListNode
#         :rtype: bool
#         """
#         if head == None:
#             return False
#
#         fast, slow = head, head
#         while fast.next != None and fast.next.next != None:
#             slow = slow.next
#             fast = fast.next.next
#             if slow == fast:
#                 return True
#
#         return False
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        h, t = head, head

        while h and h.next:
            h = h.next.next
            t = t.next
            if h == t:
                return True

        return False



if __name__ == '__main__':
    head = list_lib().makeLinkList([3,2,0,-4])
    pos = 1
    result = Solution().hasCycle(head)
    print(result)

