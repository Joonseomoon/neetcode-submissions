# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        
        while curr:
            next = curr.next # save the next to iterate 
            curr.next = prev # make the current next the previous node
            prev = curr # move the previous node to current node
            curr = next # assign current node to original next node
    
        return prev
