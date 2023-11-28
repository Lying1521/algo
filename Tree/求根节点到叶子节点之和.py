# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        total = 0
        stack = [(root,0)]
        while stack:
            node, val = stack.pop()
            if not node.left and not node.right:
                total += 10 * val + node.val
                continue
            if node.right:
                stack.append((node.right, 10*val+node.val))
            if node.left:
                stack.append((node.left, 10*val+node.val))
        return total