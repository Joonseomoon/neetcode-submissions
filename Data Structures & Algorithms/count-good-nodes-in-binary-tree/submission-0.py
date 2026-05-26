# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = [[root, root.val]]
        res = 0 

        while stack:
            node, maxNode = stack.pop()
            if node:
                if node.val >= maxNode:
                    res += 1
                stack.append([node.right, max(maxNode, node.val)])
                stack.append([node.left, max(maxNode, node.val)])
        return res