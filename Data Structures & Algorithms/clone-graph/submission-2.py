"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        copyMap = {}
        copyMap[node] = Node(node.val)
        q = deque([node])

        while q:
            curr = q.popleft()
            for neighbor in curr.neighbors:
                if neighbor not in copyMap:
                    copyMap[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                copyMap[curr].neighbors.append(copyMap[neighbor])
        return copyMap[node]