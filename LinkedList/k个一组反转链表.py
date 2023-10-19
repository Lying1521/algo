# 给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。
#
# k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
#
# 你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换

# 示例 1：
# 输入：head = [1,2,3,4,5], k = 2
# 输出：[2,1,4,3,5]

# 示例 2：
# 输入：head = [1,2,3,4,5], k = 3
# 输出：[3,2,1,4,5]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 思路  先找到第k个节点 如果有开始反转， 注意反转完一组后把链表重新连上

from util import ListNode


class Solution:
    def reverseKGroup(self, head, k):
        if not head or k <= 1:
            return head
        dummy = ListNode(-1)

        current = head
        bottom = head
        tail = dummy

        while current:
            i = 0
            foot = current
            while foot and i < k - 1:
                i += 1
                foot = foot.next

            if foot:
                for i in range(k):
                    temp = current.next
                    current.next = tail.next
                    tail.next = current
                    current = temp

                bottom.next = current

                tail = bottom
                bottom = current

            else:
                return dummy.next

        return dummy.next


