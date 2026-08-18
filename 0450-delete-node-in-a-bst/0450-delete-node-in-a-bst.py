# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def smallest(node):
            while node.left:
                node = node.left
            return node
        def deleteNode(node, val):
            if node is None:
                return
            if val < node.val:
                node.left = deleteNode(node.left, val)
            elif val > node.val:
                node.right = deleteNode(node.right,val)
            else:
                if node.left is None:
                    return node.right
                if node.right is None:
                    return node.left
                successor = smallest(node.right)
                node.val = successor.val
                node.right = deleteNode(node.right, successor.val)
            return node
        return deleteNode(root, key)

        