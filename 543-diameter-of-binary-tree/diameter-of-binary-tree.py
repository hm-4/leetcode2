# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.diameter = 0

    def dfs(self, curr_root):
        if not curr_root:
            return -1 # null root convention
        right_child_height = self.dfs(curr_root.right)
        left_child_height = self.dfs(curr_root.left)

        self.diameter = max(self.diameter, right_child_height + left_child_height + 2)

        return 1 + max(left_child_height, right_child_height)


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        height of leaf is 0
        height of null tree is -1 as convention, math works out.
        diameter = left_height + right_height + 2 (for two new edges)

        """
        self.diameter = 0 
        # global variable to store the solution
        # so that dont need to return max diameter also in the 
        # every recurssion.
        # we can use nonlocal for global variable.

        curr_root = root
        self.dfs(curr_root)
        return self.diameter
            
