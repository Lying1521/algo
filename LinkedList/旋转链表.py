# 给你一个链表的头节点head ，旋转链表，将链表每个节点向右移动k个位置。
#
# 示例 1：
# 输入：head = [1, 2, 3, 4, 5], k = 2
# 输出：[4, 5, 1, 2, 3]
# 示例2：
# 输入：head = [0, 1, 2], k = 4
# 输出：[2, 0, 1]

# 思路： 找到旋转后的其实位置，即倒数第 n =（k mod len(head))个节点
#       从倒数第n个节点开始，从头部开始依次插入

from util import ListNode


class Solution:
    def rotateRight(self, head, k):
        if not head:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        fast = head

        l = 0
        t = k
        while l < t:
            fast = fast.next
            l += 1
            if not fast:
                t = k % l
                fast = head
                l = 0

        slow = head

        while fast.next:
            fast = fast.next
            slow = slow.next

        prev = dummy
        while slow.next:
            temp = slow.next
            slow.next = slow.next.next
            temp.next = prev.next
            prev.next = temp
            prev = prev.next

        return dummy.next
