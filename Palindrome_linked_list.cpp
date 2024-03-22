/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    bool isPalindrome(ListNode* head) {
        ListNode* head1=NULL;
        ListNode* res = head;
        ListNode* temp=head1;
        while(res){
           int  x=res->val;
            ListNode* y=new ListNode(x);
            y->next=temp;
            temp=y;
            res=res->next;
        }
        while(head && temp){
            if(temp->val!=head->val){
                return false;
            }
            else{
                head=head->next;
                temp=temp->next;
            }
        }
        return true;
        
    }
};
