"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        temp = [root]
        while temp:
            temp.append(None)
            new_temp = []
            for idx, node in enumerate(temp[:-1]):
                node.next = temp[idx + 1]
                if node.left:
                    new_temp.append(node.left)
                if node.right:
                    new_temp.append(node.right)
            temp = new_temp
        return root

