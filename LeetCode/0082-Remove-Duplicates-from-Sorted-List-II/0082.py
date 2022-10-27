class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import List
from test_lib import process_link_list as list_lib

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        if not head or not head.next:
            return head

        map = {}
        while head:
            if head.val not in map:
                map[head.val] = 0
            else:
                map[head.val] += 1

            head = head.next

        pointer = ListNode(0)
        new = pointer
        for key in map:
            if map[key] == 0:
                temp = ListNode(key)
                pointer.next = temp
                pointer = pointer.next

        new = new.next

        return new


if __name__ == '__main__':
    input = [1,2,3,3,4,4,5]
    head = list_lib().makeLinkList(input)
    output = Solution().deleteDuplicates(head)
    print("Input: head = {}\nOutput : ".format(input),end='')
    list_lib().printLinkList(output)


    input = [1,1,1,2,3]
    head = list_lib().makeLinkList(input)
    output = Solution().deleteDuplicates(head)
    print("Input: head = {}\nOutput : ".format(input),end='')
    list_lib().printLinkList(output)








