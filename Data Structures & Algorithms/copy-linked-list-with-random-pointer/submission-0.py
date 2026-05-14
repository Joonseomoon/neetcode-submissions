"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node = head
        dummy = prev = Node(0)
        hashmap = {}

        while node:
            curr = Node(node.val)
            prev.next = curr
            hashmap[node] = curr
            prev = curr
            node = node.next
        node = head
        curr = dummy.next
        while node:
            curr.random = hashmap.get(node.random)
            curr = curr.next
            node = node.next

        return dummy.next