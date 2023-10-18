# 给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
#
# 字母异位词 是由重新排列源单词的所有字母得到的一个新单词。

# 示例 1:
# 输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
#
# 示例 2:
# 输入: strs = [""]
# 输出: [[""]]
#
# 示例 3:
# 输入: strs = ["a"]
# 输出: [["a"]]

class Solution:
    def groupAnagrams(self, strs):

        groups = {}
        for s in strs:
            key = [0 for i in range(26)]

            for i in s:
                key[ord(i) - ord("a")] += 1

            key = tuple(key)

            if key not in groups:
                groups[key] = []
            groups[key].append(s)

        return list(groups.values())

