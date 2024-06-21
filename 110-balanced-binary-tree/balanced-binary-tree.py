# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.bool = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.dfs(root)
        return self.bool

    def dfs(self, root):
        if not root:
            return 0
        h_l = 1 + self.dfs(root.left)
        h_r = 1 + self.dfs(root.right)
        if not (-1 <= h_l - h_r <= 1):
            self.bool = False
        if h_l < h_r:
            return h_r
        else:
            return h_l
