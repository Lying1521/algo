# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_sum = float('-inf')

        def f(node):
            if not node:
                return 0
            left = max(f(node.left), 0)
            right = max(f(node.right), 0)
            self.max_sum = max(self.max_sum, left + right + node.val)
            return max(left + node.val, right + node.val, 0)

        f(root)

        return self.max_sum
