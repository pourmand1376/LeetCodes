# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result =self.convert_to_int(l1)+self.convert_to_int(l2)
        return self.convert_to_list(result)
    
    def convert_to_int(self, node: ListNode):
        result = ""
        while node is not None:
            result =  str(node.val) + result
            node = node.next
        return int(result)
    
    def convert_to_list(self, number:int):
        number = str(number)
        node = None
        for item in number: 
            node = ListNode(int(item), next=node)
        return node