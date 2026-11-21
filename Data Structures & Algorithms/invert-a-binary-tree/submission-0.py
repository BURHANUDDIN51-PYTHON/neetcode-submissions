# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        return self.getTreeNode(root)
        

    def getTreeNode(self, root): # Get all the values 

        if root is None: return None
        left = right = None
        if root.left:
            left = self.getTreeNode(root.left)

        if root.right:
            right = self.getTreeNode(root.right)

        root.right = left 
        root.left = right 

        return root