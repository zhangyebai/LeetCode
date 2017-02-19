#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
    @Author 张夜白 At Leetcode
    Title: Add Two Numbers
    You are given two linked lists representing two non-negative numbers.
    The digits are stored in reverse order and each of their nodes contain a single digit.
    Add the two numbers and return it as a linked list.

    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8

"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def add_two_nums(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
            :type l1: ListNode
            :type l2: ListNode
            :rtype: ListNode
        """
        self.__init__()
        if l1 is None and l2 is None:
            return None
        else:
            if l1 is None:
                return l2
            elif l2 is None:
                return l1

        result_node = ListNode((l1.val + l2.val) % 10)
        carry_flag = int((l1.val + l2.val) // 10)
        l_hand, r_hand = l1.next, l2.next
        step_node = result_node
        while l_hand is not None or r_hand is not None:
            # corner case
            if l_hand is None:
                step_node.next = ListNode((r_hand.val + carry_flag) % 10)
                step_node = step_node.next
                carry_flag = (r_hand.val + carry_flag) // 10
                r_hand = r_hand.next
                continue
            elif r_hand is None:
                step_node.next = ListNode((l_hand.val + carry_flag) % 10)
                step_node = step_node.next
                carry_flag = (l_hand.val + carry_flag) // 10
                l_hand = l_hand.next
                continue

            # normal step
            step_node.next = ListNode((l_hand.val + r_hand.val + carry_flag) % 10)
            carry_flag = (l_hand.val + r_hand.val + carry_flag) // 10
            step_node = step_node.next
            r_hand, l_hand = r_hand.next, l_hand.next

        # carry case
        if carry_flag:
            step_node.next = ListNode(carry_flag)

        return result_node


    def add_two_nums2(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        step = result
        l_hand, r_hand = l1, l2
        node_sum = 0
        while l_hand is not None or r_hand is not None:
            node_sum //= 10
            if l_hand is not None:
                node_sum += l_hand.val
                l_hand = l_hand.next

            if r_hand is not None:
                node_sum += r_hand.val
                r_hand = r_hand.next

            step.next = ListNode(node_sum % 10)
            step = step.next

        if node_sum // 10 > 0:
            step.next = ListNode(1)

        return result.next


def init_node(param)->ListNode:
    result_node, temp_node = None, None
    for value in param:
        if result_node is None:
            temp_node = ListNode(value)
            result_node = temp_node
            continue
        temp_node.next = ListNode(value)
        temp_node = temp_node.next

    return result_node


def print_node(param_node: ListNode)->None:
    temp_node, values = param_node, []
    while temp_node is not None:
        values.append(str(temp_node.val))
        temp_node = temp_node.next
    print('[', '->'.join(values), ']', sep=None)

if __name__ == '__main__':
    l_node = init_node([3, 7])
    r_node = init_node([9, 2])

    print_node(Solution().add_two_nums(l_node, r_node))



