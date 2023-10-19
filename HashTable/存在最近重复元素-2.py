
# 给你一个整数数组 nums 和一个整数 k ，判断数组中是否存在两个 不同的索引 i 和 j ，满足 nums[i] == nums[j] 且 abs(i - j) <= k 。
# 如果存在，返回 true ；否则，返回 false 。


class Solution:
    def containsNearbyDuplicate(self, nums, k):
        d = {}
        for idx, n in enumerate(nums):
            if n not in d:
                d[n] = idx
            else:
                if idx - d[n] <= k:
                    return True
                else:
                    d[n] = idx

        return False
