# 给定一个已排序的链表的头 head ， 删除原始链表中所有重复数字的节点，只留下不同的数字 。返回 已排序的链表 。

# 示例 1：
# 输入：head = [1,2,3,3,4,4,5]
# 输出：[1,2,5]
# 示例 2：
# 输入：head = [1,1,1,2,3]
# 输出：[2,3]

# 思路：双指针，第一个指针记录未重复的最后一个元素，
#            另一个指针遍历所有元素比较和后继的值，若不同则第一个指针后移，相同则只有比较指针后移，直到下一个不同

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from util import ListNode


class Solution:
    def deleteDuplicates(self, head):
        dummy = ListNode(-1)
        dummy.next = head
        current = head
        prev = dummy
        while current and current.next:
            if current.val == current.next.val:
                current = current.next
            else:
                if prev.next != current:
                    current = current.next
                    prev.next = current
                else:
                    prev = prev.next
                    current = current.next
        if current and prev.next != current:
            prev.next = None

        return dummy.next
