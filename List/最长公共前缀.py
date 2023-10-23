# s编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。

# 示例 1：
# 输入：strs = ["flower","flow","flight"]
# 输出："fl"

# 示例 2：
# 输入：strs = ["dog","racecar","car"]
# 输出：""
# 解释：输入不存在公共前缀。

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        common = strs.__getitem__(0)
        for idx, s in enumerate(strs):
            n = min(len(s), len(common))
            temp = ""
            for i in range(n):
                if common.__getitem__(i) == s.__getitem__(i):
                    temp += common.__getitem__(i)
                else:
                    break
            if temp != "":
                common = temp
            else:
                return ""

        return common
