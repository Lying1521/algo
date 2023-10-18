#
# 在股票交易中，如果前一天的股价高于后一天的股价，则可以认为存在一个「交易逆序对」。
# 请设计一个程序，输入一段时间内的股票交易记录 record，返回其中存在的「交易逆序对」总数。

# 示例 1:
#
# 输入：record = [9, 7, 5, 4, 6]
# 输出：8
# 解释：交易中的逆序对为 (9, 7), (9, 5), (9, 4), (9, 6), (7, 5), (7, 4), (7, 6), (5, 4)。

# 思路： 分治， 使用归并排序， 当合并两个有序子集，比较时如果左侧出现大于右侧的数，
#       由于部分有序，则左侧剩余数都大于右侧当前值，即为mid-i个逆序对
#       此题重点总结归并排序代码框架。

class Solution:
    def reversePairs(self, record) -> int:
        counts = self.merge_sort_child(record, 0, len(record))
        return counts

    def merge_sort_child(self, nums, left, right):
        if right <= left + 1:
            return 0

        mid = left + (right-left) // 2
        c_l = self.merge_sort_child(nums, left, mid)
        c_r = self.merge_sort_child(nums, mid, right)
        temp = []
        i = left
        j = mid
        c = 0
        while i < mid and j < right:
            if nums[i] <= nums[j]:
                temp.append(nums[i])
                i += 1
            else:
                temp.append(nums[j])
                c += mid - i
                j += 1

        if i < mid:
            temp = temp + nums[i:mid]
        if j < right:
            temp = temp + nums[j:right]
        nums[left:right] = temp[:]
        return c + c_r + c_l
