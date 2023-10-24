# 如果在将所有大写字符转换为小写字符、并移除所有非字母数字字符之后，短语正着读和反着读都一样。则可以认为该短语是一个 回文串 。
# 字母和数字都属于字母数字字符。
# 给你一个字符串 s，如果它是 回文串 ，返回 true ；否则，返回 false 。

# 思路：头尾双指针
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        s = list(s)
        while left < right:
            s_left = s[left].lower()
            s_right = s[right].lower()
            if not s_left.isalnum():
                left += 1
                continue
            if not s_right.isalnum():
                right -= 1
                continue
            if s_left != s_right:
                return False
            right -= 1
            left += 1

        return True