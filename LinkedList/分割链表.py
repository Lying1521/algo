# 给你一个链表的头节点head和一个特定值x ，请你对链表进行分隔，使得所有小于x的节点都出现在大于或等于x的节点之前。
# 你应当保留两个分区中每个节点的初始相对位置。
#
# 示例 1：
# 输入：head = [1, 4, 3, 2, 5, 2], x = 3
# 输出：[1, 2, 2, 4, 3, 5]
# 示例 2：
# 输入：head = [2, 1], x = 2
# 输出：[1, 2]

# 思路： 找到第一个大于等于x的节点，其前驱为第一个小于x的节点
#       从起后继开始判断，小于x则插入第一个小于x的节点之后

from util import ListNode


class Solution:
    def partition(self, head, x):
        if not head:
            return head
        dummy = ListNode(-1)
        dummy.next = head

        current = head
        prev = dummy

        while current and current.val < x:
            current = current.next
            prev = prev.next

        if not current:
            return head

        below = prev
        high = current

        current = current.next

        while current:
            if current.val >= x:
                high = high.next
            else:
                temp = current
                high.next = current.next

                temp.next = below.next
                below.next = temp
                below = below.next
            current = high.next

        return dummy.next

