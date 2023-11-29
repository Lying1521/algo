# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        cur = root
        while cur:
            self.stack.append(cur)
            cur = cur.left

    def next(self):
        """
        :rtype: int
        """
        cur = self.stack.pop()
        node = cur.right
        while node:
            self.stack.append(node)
            node = node.left

        return cur.val

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.stack:
            return True

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()