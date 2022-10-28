# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import List
from utility.test_lib import process_link_list as list_lib

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        if not l1 or not l2 :
            return l1 or l2

        head = ListNode(0)
        answer = head
        carry = 0

        while l1 and l2:
            add = l1.val + l2.val + carry
            carry = int(add /10)
            head.next = ListNode(add % 10)
            head = head.next
            l1, l2 = l1.next, l2.next
        l = l1 if l1 else l2
        while l:
            add = l.val + carry
            carry = int(add / 10)
            head.next = ListNode(add % 10)
            head = head.next
            l = l.next
        if carry:
            head.next = ListNode(1)
        return answer.next

if __name__ == '__main__':

    l1 = list_lib().makeLinkList([2,4,3])
    l2 = list_lib().makeLinkList([5,6,4])

    result = Solution().addTwoNumbers(l1, l2)
    
    print("Input: l1 = [2,4,3], l2 = [5,6,4]\nOutput : ",end='')
    list_lib().printLinkList(result)
    