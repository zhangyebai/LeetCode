
/**
 * Created by Zhang-YeBai on 2017/2/19.
 */
public class AddTwoNumbers {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {

        ListNode result = new ListNode(0);
        ListNode step = result;
        ListNode l_hand = l1;
        ListNode r_hand = l2;
        int node_sum = 0;
        for(;l_hand != null || r_hand != null;){
            node_sum /= 10;
            if (l_hand != null){
                node_sum += l_hand.val;
                l_hand = l_hand.next;
            }

            if (r_hand !=null){
                node_sum += r_hand.val;
                r_hand = r_hand.next;
            }

            step.next = new ListNode(node_sum % 10);
            step = step.next;
        }
        if (node_sum / 10 > 0){
            step.next = new ListNode(1);
        }
        return result.next;
        /*int carry_flag = (l1.val + l2.val) / 10;
        ListNode l_hand = l1.next;
        ListNode r_hand = l2.next;
        ListNode step_node = result;
        for(;l_hand != null || r_hand != null;){
            if(l_hand == null){
                step_node.next = new ListNode((r_hand.val + carry_flag) % 10);
                step_node = step_node.next;
                carry_flag = (r_hand.val + carry_flag) / 10;
                r_hand = r_hand.next;
                continue;
            }else if(r_hand == null){
                step_node.next = new ListNode((l_hand.val + carry_flag) % 10);
                step_node = step_node.next;
                carry_flag = (l_hand.val + carry_flag) / 10;
                l_hand = l_hand.next;
                continue;
            }
            step_node.next = new ListNode((l_hand.val + r_hand.val + carry_flag) % 10);
            carry_flag = (l_hand.val + r_hand.val + carry_flag) / 10;
            step_node = step_node.next;
            r_hand =  r_hand.next;
            l_hand =l_hand.next;
        }

        if(carry_flag > 0){
            step_node.next = new ListNode(carry_flag);
        }

        return result;*/
    }
    public static void main(String[] args){
        int[] arr1 = {1,6,6,0,5,8,1,0,7};
        int[] arr2 = {8,2,5,7,9,1,0,2,2,1};
        ListNode l1 =  initList(arr1);
        ListNode l2 = initList(arr2);
        printNode(new AddTwoNumbers().addTwoNumbers(l1, l2));
    }

    public static ListNode initList(int[] arr){
        ListNode node = new ListNode(arr[0]);
        ListNode step = node;
        for(int index = 1; index < arr.length;++index){
            step.next = new ListNode(arr[index]);
            step = step.next;
        }
        return node;
    }

    public static void printNode(ListNode node){
        while (node != null){
            System.out.println(node.val);
            node = node.next;
        }
    }
}

class ListNode {
     int val;
      ListNode next;
      ListNode(int x) { val = x; }
}
