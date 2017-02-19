#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
    @Author 张夜白 At LeetCode  self.__init__()是为了防止提示class method should be static method
    container-with-most-water: Given n non-negative integers a1, a2, ..., an,
    where each represents a point at coordinate (i, ai). n vertical lines are drawn such that
     the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis
      forms a container, such that the container contains the most water.

    Note: You may not slant the container.
"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        self.__init__()
        max_area = 0
        length = len(height)
        left, right = 0, length - 1
        while (left >= 0) and (right <= length - 1) and (left < right):
            max_area = max(max_area, min(height[left], height[right]) * abs(left - right))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return max_area

    # 暴力枚举，后面的话我不造说啥了
    # 提交的时候TLE了
    def maxArea_Brute(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        self.__init__()
        length = len(height)
        max_area = 0
        for i in range(length):
            for j in range(i + 1, length):
                max_area = max(max_area, abs(height[i], height[j]) * (j - i))
        return max_area

if __name__ == '__main__':
    pass
