#!/usr/bin/env python
# _*_ coding:utf-8 _*_


class Solution(object):
    """
    def threeSum(self, nums):

        :type nums: List[int]
        :rtype: List[List[int]]

        # pre, mid, after = 0, 0, 0
        length = len(nums)
        result = []
        if length < 3:
            return result
        elif length == 3:
            if sum(nums) == 0:
                result.append(nums)
                return result

        for i in range(0, length - 3):
            pre = nums[i]
            for j in range(i + 1, length - 2):
                mid = nums[j]
                for k in range(j + 1, length - 1):
                    if nums[k] == (0 - (pre + mid)):
                        result.append([pre, mid, nums[k]])
        return list(set(result))
        """
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        length = len(nums)
        result = []
        if length < 3:
            return result
        elif length == 3:
            if sum(nums) == 0:
                result.append(nums)
                return result
        for i in range(0, length - 2):
            if i and nums[i] == nums[i - 1]:
                continue
            target = -nums[i]
            left, right = i + 1, length - 1
            while left < right:
                if nums[left] + nums[right] == target:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    left += 1
        return result

