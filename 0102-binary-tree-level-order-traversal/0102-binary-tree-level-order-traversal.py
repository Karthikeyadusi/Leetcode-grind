# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def bfs(root):
            if root is None:
                return []
            res = []
            queue = deque([root])
            while queue:
                level = []
                size = len(queue)
                for i in range(size):
                    node = queue.popleft()
                    level.append(node.val)
                    if node.left is not None:
                        queue.append(node.left)
                    if node.right is not None:
                        queue.append(node.right)
                res.append(level)
            return res
        return bfs(root)

        