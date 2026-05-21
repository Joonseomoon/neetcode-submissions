# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = prevEnd = ListNode(0)
        while head:
            start = head
            validGroup = True
            for i in range(k - 1):
                head = head.next
                if not head:
                    validGroup = False
                    break
            if not validGroup:
                prevEnd.next = start
                break
            prevEnd.next = head
            temp = head.next if head else None
            head.next = None
            self.reverseList(start)
            prevEnd = start
            head = temp
        return dummy.next

    def reverseList(self, head):
        node = head
        prev = None
        while node:
            temp = node.next
            node.next = prev
            prev = node
            node = temp
        return node
