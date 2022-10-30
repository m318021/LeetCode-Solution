# 1. Two Sum - Easy 
# https://leetcode.com/problems/two-sum/



from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class process_link_list:
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





if __name__ == '__main__':

    l1 = process_link_list().makeLinkList([2,4,3])
    l2 = process_link_list().makeLinkList([5,6,4])

    Solution().printLinkList(l1)

