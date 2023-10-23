# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

# 示例 1：
# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6
# 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
#
# 示例 2：
# 输入：height = [4,2,0,3,2,5]
# 输出：9

# 思路： 借助栈，当前元素小于栈顶则入栈，栈内一定递减
#       当前元素大于栈顶时，出栈。
#       如果把可接水的区域视作一个桶，出栈元素则为桶底高度，新的栈顶和当前元素的较小值为桶顶，当前元素和栈顶元素下标差-1为桶宽度
#       新增的雨水量为 （桶顶高度-桶底高度） * 桶宽度
#       注：当需要回看的时候最好借助栈，入栈内容无意义只需要宽度时，可以只记录长度。

class Solution:
    def trap(self, height) -> int:
        stack = []
        total = 0
        for idx, h in enumerate(height):
            while stack and height[stack[-1]] < h:
                top = stack.pop()
                if not stack:
                    break
                wight = idx - stack[-1] - 1
                high = min(height[stack[-1]], h) - height[top]
                total += wight * high
            stack.append(idx)
        return total





