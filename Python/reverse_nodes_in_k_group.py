#!/usr/bin/env python
# _*_ coding:utf-8 _*_


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        list_count = 0
        curr = head
        while curr:
            list_count += 1
            curr = curr.next
        if list_count == 0 or list_count < k or k == 1:
            return head

        result = ListNode(0)
        result.next = head
        rever = result
        curr = result.next
        while k <= list_count:
            group_count = k
            link_node = curr
            while group_count:
                temp = curr
                curr = curr.next
                temp.next = result.next
                result.next = temp
                group_count -= 1
            link_node.next = curr
            result = link_node
            list_count -= k
        return rever.next

if __name__ == '__main__':
    p = ListNode(0)
    t = p
    t.next = ListNode(1)
    t.next.next = ListNode(2)
    s = Solution().reverseKGroup(p, 2)
    print(s)
    while s:
        print(s.val)
        s = s.next