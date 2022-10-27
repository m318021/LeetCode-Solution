class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import List
from test_lib import process_link_list as list_lib

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # Method 1
        # if not head or not head.next:
        #     return head
        # head.next = self.deleteDuplicates(head=head.next)
        # return head if head.val != head.next.val else head.next

        # Method 2
        if not head or not head.next:
            return head

        new_list = ListNode(head.val)
        flag = head.val

        pointer = new_list

        while head:
            if head.val != flag:
                temp = ListNode(head.val)
                new_list.next = temp
                new_list = new_list.next
                flag = head.val

            head = head.next

        return pointer

if __name__ == '__main__':
    input = [1, 1, 2]
    head = list_lib().makeLinkList(input)
    output = Solution().deleteDuplicates(head)
    print("Input: l1 = {}\nOutput : ".format(input),end='')
    list_lib().printLinkList(output)


    input = [1, 1, 2, 3, 3]
    head = list_lib().makeLinkList(input)
    output = Solution().deleteDuplicates(head)
    print("Input: l1 = {}\nOutput : ".format(input),end='')
    list_lib().printLinkList(output)








