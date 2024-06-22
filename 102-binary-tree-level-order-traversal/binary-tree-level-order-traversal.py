# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return []
        
        level_nodes = [root] # stores the current level nodes
        while len(level_nodes) > 0:
            val_list = []
            new_level_nodes = []
            for node in level_nodes:
                val_list.append(node.val)
                if node.left:
                    new_level_nodes.append(node.left)
                if node.right:
                    new_level_nodes.append(node.right)
            level_nodes = new_level_nodes
            res.append(val_list)

        return res
