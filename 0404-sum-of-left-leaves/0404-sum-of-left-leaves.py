# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def sumoflefts(node):
            value = 0
            if node is None:
                return 0
            if node.left:
                if node.left.left is None and node.left.right is None:
                    value = node.left.val
            left = sumoflefts(node.left)
            right = sumoflefts(node.right)
            return value + left + right
        return sumoflefts(root)

            
        