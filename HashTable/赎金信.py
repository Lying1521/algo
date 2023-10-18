# 给你两个字符串：ransomNote和magazine，
# 判断ransomNote能不能由magazine里面的字符构成。
# 如果可以，返回true ；否则返回false。
# magazine中的每个字符只能在ransomNote中使用一次。
#
# 示例 1：
# 输入：ransomNote = "a", magazine = "b"
# 输出：false
#
# 示例 2：
# 输入：ransomNote = "aa", magazine = "ab"
# 输出：false
#
# 示例 3：
# 输入：ransomNote = "aa", magazine = "aab"
# 输出：true

# 思路遍历magazine,使用dict记录每个字符，遍历ransomNote判断是够有该字符

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = {}
        for s in magazine:
            if s not in d:
                d[s] = 0
            d[s] += 1

        for s in ransomNote:
            if s not in d:
                return False
            elif d[s] == 0:
                return False
            else:
                d[s] -= 1
        return True
