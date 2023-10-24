# 给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0 开始）。
# 如果 needle 不是 haystack 的一部分，则返回  -1 。

# 示例 1：
# 输入：haystack = "sadbutsad", needle = "sad"
# 输出：0
# 解释："sad" 在下标 0 和 6 处匹配。
# 第一个匹配项的下标是 0 ，所以返回 0 。
#
# 示例 2：
# 输入：haystack = "leetcode", needle = "leeto"
# 输出：-1
# 解释："leeto" 没有在 "leetcode" 中出现，所以返回 -1 。

# 思路：用栈做回溯，栈内为已匹配元素。

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1

        stack = []
        idx = 0
        while idx < len(haystack):
            s = haystack[idx]
            if s == needle.__getitem__(len(stack)):
                stack.append(s)
                if len(stack) == len(needle):
                    return idx - len(needle) + 1
            else:
                idx -= len(stack)
                stack = []

            idx += 1

        return -1
