#pragma once
//#include <tchar.h>
#ifndef NULL
#ifdef __cplusplus
#define NULL 0
#else
#define NULL ((void *)0)
#endif
#endif

struct ListNode {
	int val;
	ListNode *next;
	ListNode(int x) : val(x), next(NULL) {}
	
};
class AddTwoNumbers {
public:
	ListNode* addTwoNumbers(ListNode* l1, ListNode* l2)
	{
		ListNode head(0);
		ListNode *step = &head, *l_hand = l1, *r_hand = l2;
		int node_sum = 0;
		for (; l_hand || r_hand;) 
		{
			node_sum /= 10;
			if (l_hand) 
			{
				node_sum += l_hand->val;
				l_hand = l_hand->next;
			}

			if (r_hand) 
			{
				node_sum += r_hand->val;
				r_hand = r_hand->next;
			}

			step->next = new ListNode(node_sum % 10);
			step = step->next;
		}
		if (node_sum / 10 > 0)
		{
			step->next = new ListNode(1);
		}

		return head.next;
	}
};