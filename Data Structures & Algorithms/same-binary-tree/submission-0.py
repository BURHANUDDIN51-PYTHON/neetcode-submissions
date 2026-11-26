# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(a, b):
            # Base case 
            if not a and not b: 
                return True

            # Change case 
            if (not a and b) or (a and not b) or (a.val != b.val):
                return False

            left, right = dfs(a.left, b.left), dfs(a.right, b.right)

            return left and right

        return dfs(p, q)