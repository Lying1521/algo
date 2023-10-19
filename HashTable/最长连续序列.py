# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
#
# 请你设计并实现时间复杂度为 O(n) 的算法解决此问题。


# 示例 1：
# 输入：nums = [100,4,200,1,3,2]
# 输出：4
# 解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。

# 示例 2：
# 输入：nums = [0,3,7,2,5,8,4,6,0,1]
# 输出：9

# 思路 任意一个新数组 都可能连接左侧或右侧已存在的区间，若连接上则，则更新左侧或右侧区间端点的长度。 有点像归并的思路

class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0

        max_length = 0
        d = {}
        for idx, n in enumerate(nums):
            if n not in d:
                left = d.get(n - 1, 0)
                right = d.get(n + 1, 0)
                current = left + right + 1

                if current > max_length:
                    max_length = current

                d[n] = 1
                d[n - left] = current
                d[n + right] = current

        return max_length







