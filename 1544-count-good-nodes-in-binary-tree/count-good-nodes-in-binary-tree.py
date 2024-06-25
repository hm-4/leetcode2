# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = 0
    def goodNodes(self, root: TreeNode) -> int:
        
        return self.dfs(root, root.val)

    def dfs(self, root, max_uptil_now):
        if not root:
            return 0
        # print(root.val)
        res = 0
        if max_uptil_now <= root.val:
            res += 1
            max_uptil_now = root.val
            # print("max_uptil_now: ", max_uptil_now)
            # print("count: ", self.count)
            

        res += self.dfs(root.left, max_uptil_now)
        res += self.dfs(root.right, max_uptil_now)
        return res
