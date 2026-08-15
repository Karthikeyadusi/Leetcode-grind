# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def issame(p,q):
            if p is None and q is None:
                return True
            elif p is None or q is None:
                return False
            else:
                return p.val == q.val and issame(p.left, q.left) and issame(p.right, q.right)
        def issubroot(root, subRoot):
            if root is None and subRoot is None:
                return True
            elif root is None or subRoot is None:
                return False
            return issame(root, subRoot) or issubroot(root.left, subRoot) or issubroot(root.right, subRoot)
        return issubroot(root, subRoot)

        