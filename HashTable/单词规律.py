# 给定一种规律 pattern 和一个字符串 s ，判断 s 是否遵循相同的规律。
# 这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 s 中的每个非空单词之间存在着双向连接的对应规律。

# 示例1:
# 输入: pattern = "abba", s = "dog cat cat dog"
# 输出: true

# 示例 2:
# 输入:pattern = "abba", s = "dog cat cat fish"
# 输出: false

# 示例 3:
# 输入: pattern = "aaaa", s = "dog cat cat dog"
# 输出: false

# 思路： 空分割，2个dict维护模式和单词之间的相互映射关系

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.strip().split(" ")
        if len(words) != len(pattern):
            return False
        p2w = {}
        w2p = {}
        for idx, p in enumerate(pattern):
            if p not in p2w and words[idx] not in w2p:
                p2w[p] = f"{p}:{words[idx]}"
                w2p[words[idx]] = f"{p}:{words[idx]}"
            else:
                if p2w.get(p, "") != w2p.get(words[idx], ""):
                    return False
        return True