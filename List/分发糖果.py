# -*- coding:UTF-8 -*-

# author:Li Yu
# datetime: 2023/10/22 17:37
# software: PyCharm

# n 个孩子站成一排。给你一个整数数组 ratings 表示每个孩子的评分。
#
# 你需要按照以下要求，给这些孩子分发糖果：
#
# 每个孩子至少分配到 1 个糖果。
# 相邻两个孩子评分更高的孩子会获得更多的糖果。
# 请你给每个孩子分发糖果，计算并返回需要准备的 最少糖果数目 。

# 思路： 数组中应存在递增区间和递减区间， 每次遍历决定下一个值的大小
#       如果递增，则分配值+1。
#       如果出现递减，当前值为递减序列起点，暂时保留，入栈（由于元素无意义，可以只记录递减长度，不入栈，加上递减长度即可）
#       特殊情况在于 递减转向递增时，如果当前递减长度和最近递增长度（起点时保留的值）的较大值为递减起点的分配值
#       有一点点回溯的感觉在里面，优化后没有的回溯步骤。

class Solution:
    def candy(self, ratings) -> int:
        print(ratings)
        desc = 0
        total = 0
        candy = 1
        temp = 0
        for idx, r in enumerate(ratings[:-1]):
            print(r, desc, total)
            if r > ratings[idx + 1]:
                temp = candy
                desc += 1
                total += desc
            else:
                if desc:
                    total += max(desc + 1, temp)
                    candy = 1
                else:
                    total += candy
                if r == ratings[idx + 1]:
                    candy = 0
                candy += 1
                desc = 0
                temp = 0
            print(r, desc, total, candy, temp)

        if desc:
            total += max(desc + 1, temp)
        else:
            total += candy

        return total



