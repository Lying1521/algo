
# 数组中的第k个最大元素

# 给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
#
# 请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
#
# 你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。

# 示例 1:
#
# 输入: [3,2,1,5,6,4], k = 2
# 输出: 5
# 示例 2:
#
# 输入: [3,2,3,1,2,4,5,5,6], k = 4
# 输出: 4

# 思路： 标准快排求解
#       快排超时，考虑堆排序、桶、或计数排序

class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        n = len(nums)
        num = self.quick_sort(nums, 0, len(nums)-1, n+1-k)
        return num

    def quick_sort(self, nums, left, right, k):
        p = nums[left]
        i = left
        j = right
        while i < j:
            while nums[j] >= p and i < j:
                j -= 1
            nums[i] = nums[j]

            while nums[i] < p and i < j:
                i += 1
            nums[j] = nums[i]
        nums[i] = p
        print(nums, left, right, i)
        if i+1 == k:
            return nums[i]
        elif i+1 > k:
            return self.quick_sort(nums, left, i-1, k)
        elif i+1 < k:
            return self.quick_sort(nums, i+1, right, k)

