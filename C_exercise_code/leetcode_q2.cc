 // Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int sum = 0;
        int carry = 0;
        ListNode *l3 = new ListNode(0);
        ListNode *result = l3;
        while (l1 != nullptr || l2 != nullptr){
            l3->next = new ListNode(carry);
            l3 = l3->next;
            if (l1 != nullptr && l2 == nullptr){
                sum = l1->val+l3->val;
                l1 = l1->next;
            }
            else if (l1 == nullptr && l2 != nullptr){
                sum = l2->val+l3->val;
                l2 = l2->next;
            }
            else{
                sum = l1->val+l2->val+l3->val;
                l1 = l1->next;
                l2 = l2->next;
            } 
            carry = sum/10;
            sum %= 10;
            l3->val = sum;
        }
        if (carry != 0){
            l3->next = new ListNode(carry);
            l3 = l3->next;
        }
        return result->next;
    }
};