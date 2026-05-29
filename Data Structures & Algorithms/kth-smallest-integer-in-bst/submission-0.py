# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = -1 
        self.k = k
        self.cnt = 0
        def dfs(node): # returns nth smallest value index
            if not node: return 0
            dfs(node.left)
            self.cnt += 1
            if self.cnt == self.k:
                self.res = node.val
            dfs(node.right)
            
        dfs(root)
        return self.res