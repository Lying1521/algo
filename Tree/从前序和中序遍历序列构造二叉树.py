# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None
        root = preorder[0]
        idx = inorder.index(root)
        left = self.buildTree(preorder[1:idx + 1], inorder[0:idx])
        right = self.buildTree(preorder[idx + 1:], inorder[idx + 1:])
        return TreeNode(root, left, right)

