# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
#
# 注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。

# 示例 1:
# 输入: s = "anagram", t = "nagaram"
# 输出: true

# 示例 2:
# 输入: s = "rat", t = "car"
# 输出: false

# 思路 遍历s, dict记录字母及出现次数， 遍历t 出现则减少次数

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d = {}
        for i in s:
            if i not in d:
                d[i] = 0
            d[i] += 1
        for i in t:
            if i not in d:
                return False
            else:
                d[i] -= 1
                if d[i] < 0:
                    return False
        return True