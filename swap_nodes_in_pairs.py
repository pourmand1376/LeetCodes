# https://leetcode.com/problems/swap-nodes-in-pairs/
# I couldn't solve this by myself. 

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        item = [self.val]
        while self.next is not None:
            self = self.next
            item.append(self.val)
        return str(item)

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        dummyNode = ListNode()
        previous_node = dummyNode
        curent_node = head
        while curent_node and curent_node.next:
            previous_node.next = curent_node.next
            curent_node.next = previous_node.next.next
            previous_node.next.next = curent_node

            previous_node = curent_node
            curent_node = curent_node.next

        return dummyNode.next

graph =ListNode(1,next=ListNode(2,next=ListNode(3,next=ListNode(4))))
print(Solution().swapPairs(graph))

graph =ListNode(1,next=ListNode(2)) 
print(Solution().swapPairs(graph))

