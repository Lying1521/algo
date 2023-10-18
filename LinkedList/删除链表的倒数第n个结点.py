# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

# 示例 1：
# 输入：head = [1, 2, 3, 4, 5], n = 2
# 输出：[1, 2, 3, 5]
# 示例 2：
#
# 输入：head = [1], n = 1
# 输出：[]
# 示例 3：
#
# 输入：head = [1, 2], n = 1
# 输出：[1]

# 思路： 快慢指针相差n个节点即可
from util import ListNode


class Solution:
    def removeNthFromEnd(self, head, n: int):
        dummy = ListNode(-1)
        dummy.next = head
        fast = head
        for i in range(n - 1):
            print(fast.val)
            fast = fast.next

        prev = dummy
        while fast.next:
            prev = prev.next
            fast = fast.next

        del_node = prev.next
        prev.next = prev.next.next
        del_node.next = None
        return dummy.next
