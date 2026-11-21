# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.getMaxDepth(root, 0)


    def getMaxDepth(self, root, depth):
        if root is None:
            return depth
        depth += 1

        # Get max depth from each side 
        leftDepth = self.getMaxDepth(root.left, depth)
        rightDepth = self.getMaxDepth(root.right, depth)

        return max(leftDepth, rightDepth)
