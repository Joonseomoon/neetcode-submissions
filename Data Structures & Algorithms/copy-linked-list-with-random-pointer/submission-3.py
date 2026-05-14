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
        oldToCopy = {}
        node = head
        while node:
            copy = Node(node.val)
            oldToCopy[node] = copy
            node = node.next

        node = head
        while node:
            copy = oldToCopy.get(node)
            copy.next = oldToCopy.get(node.next)
            copy.random = oldToCopy.get(node.random)
            node = node.next

        return oldToCopy.get(head)