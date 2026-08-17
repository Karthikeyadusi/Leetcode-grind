# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        def bfs(root):

            queue = deque([root])
            res = []

            while queue:
                size = len(queue)
                level = []

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


        