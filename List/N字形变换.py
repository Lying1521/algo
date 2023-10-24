# 将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
#
# 比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：
#
# 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。
#
# 请你实现这个将字符串进行指定行数变换的函数：、
#
#
# 示例 1：
# 输入：s = "PAYPALISHIRING", numRows = 3
# 输出："PAHNAPLSIIGYIR"
#
# 示例 2：
# 输入：s = "PAYPALISHIRING", numRows = 4
# 输出："PINALSIGYAHRPI"
#
# 示例 3：
# 输入：s = "A", numRows = 1
# 输出："A"

# 思路： 找规律 rows - 1 为一组 恰好 2组为一循环。 寻找组之间下标变化的规律

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        n = numRows - 1
        res = ""

        for i in range(0, len(s), 2 * n):
            res += s.__getitem__(i)

        for row in range(1, numRows - 1):
            for i in range(row, len(s), 2 * n):
                res += s.__getitem__(i)
                if i + 2 * (n - row) < len(s):
                    res += s.__getitem__(i + 2 * (n - row))

        for i in range(n, len(s), 2 * n):
            res += s.__getitem__(i)

        return res
