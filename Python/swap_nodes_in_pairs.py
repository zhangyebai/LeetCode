#!/usr/bin/env python
# _*_ coding:utf-8 _*_


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            curr = pre.next
            after = curr.next
            pre.next, after.next, curr.next = after, curr, after.next
            pre = curr
        return self.next