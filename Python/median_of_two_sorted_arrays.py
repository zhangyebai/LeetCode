#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
    @Author 张夜白 At LeetCode
    There are two sorted arrays nums1 and nums2 of size m and n respectively.
    Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
    Example 1:
        nums1 = [1, 3]
        nums2 = [2]
        The median is 2.0

    Example 2:
        nums1 = [1, 2]
        nums2 = [3, 4]
        The median is (2 + 3)/2 = 2.5
"""


class Solution(object):
    def findMedianSortedArrays(self, nums1: list, nums2: list)->float:
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        self.__init__()
        merge_list = nums1 + nums2
        merge_list.sort()
        length = len(merge_list)

        if length % 2 == 0:
            result = (merge_list[length//2] + merge_list[length//2 - 1]) / 2.0
        else:
            result = merge_list[length//2] / 1.0
        return result


if __name__ == '__main__':
    print(Solution().findMedianSortedArrays([1, 3], [2]))
