# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append(root)
        maxDepth = 0

        while len(queue) > 0:
            node = queue.popleft()

            # Get the max lenghts for each side 
            right = self.getMaxDepth(node.right)
            left = self.getMaxDepth(node.left)

            pathLen = left + right 
            if pathLen >= maxDepth:
                maxDepth = pathLen
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

        return maxDepth

    # Helper function 
    def getMaxDepth(self, root, depth = 0):
        if root is None: 
            return depth 
               
        depth += 1
        leftDepth = self.getMaxDepth(root.left, depth)
        rightDepth = self.getMaxDepth(root.right, depth)


        return max(leftDepth,rightDepth)