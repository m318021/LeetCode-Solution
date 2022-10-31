from typing import List
from utility.test_lib import process_link_list as list_lib
from utility.test_lib import ListNode

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> [ListNode]:

        listA, listB = headA, headB
        while listA!=listB:
            listA = listA.next if listA else headB
            listB = listB.next if listB else headA

        return listA



if __name__ == '__main__':
    listA =  list_lib().makeLinkList([4,1,8,4,5])
    listB =  list_lib().makeLinkList([5,6,1,8,4,5])

    output = Solution().getIntersectionNode(listA, listB)
    list_lib().printLinkList(output)


    listA =  list_lib().makeLinkList([1, 9, 1, 2, 4])
    listB =  list_lib().makeLinkList([3, 2, 4])

    output = Solution().getIntersectionNode(listA, listB)
    list_lib().printLinkList(output)

