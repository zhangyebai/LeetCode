#!/usr/bin/env python
# _*_ coding:utf-8 _*_


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        length = len(lists)
        if length == 1:
            return lists[0]

        # 二分合并，将原list拆分
        mid = length // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])

        pre = ListNode(0)
        cur = pre
        while left or right:
            if not right or (left and left.val < right.val):
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next
        return pre.next