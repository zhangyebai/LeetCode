#!/usr/bin/env python
# _*_ coding:utf-8 _*_


class Solution(object):
    # 直接pop出重复的元素，耗时较长。。
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length <= 0:
            return length
        curr = nums[0]
        index = 1
        while index < len(nums):
            if curr == nums[index]:
                nums.pop(index)
            else:
                curr = nums[index]
                index += 1
        return len(nums)

    def removeDuplicatesByReSort(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length <= 1:
            return length
        index = 0
        for i in range(1, length):
            if nums[index] != nums[i]:
                index += 1
                nums[index] = nums[i]
        return index + 1


if __name__ == '__main__':
    s = [1, 1, 2]
    print(s[:Solution().removeDuplicates(s)])
