# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.subRoot = None
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.subRoot = subRoot
        return self.dfs(root)

    def dfs(self, root):
        if not root:
            return False
        if root.val == self.subRoot.val:

            if self.ddfs(root.left, self.subRoot.left) and self.ddfs(root.right, self.subRoot.right):
                return True
        return self.dfs(root.left) or self.dfs(root.right)
        
    def ddfs(self, root1, root2):
        if not root1 and not root2:
            return True
        if (not root1 and root2) or (root1 and not root2) or (root1.val != root2.val):
            return False
        return self.ddfs(root1.left, root2.left) and self.ddfs(root1.right, root2.right)