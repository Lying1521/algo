# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder:
            return None
        val = postorder.pop()
        mid = inorder.index(val)
        root = TreeNode(val, self.buildTree(inorder[:mid], postorder[:mid]),
                        self.buildTree(inorder[mid + 1:], postorder[mid:]))
        return root

