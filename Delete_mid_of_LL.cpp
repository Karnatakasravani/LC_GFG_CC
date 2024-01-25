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
    ListNode* deleteMiddle(ListNode* head) {
        ListNode* temp=head;
        int c=0;
        while(temp)
        {
            c+=1;
            temp=temp->next;
        }
        ListNode* temp1=head;
        // ListNode* fast=head;
        int mid=c/2;
        for(int i=1;i<mid;i++)
        {
            temp1=temp1->next;
        }
        // return temp1;
        ListNode* slow=head;
        ListNode* fast=head;
        while(fast!=NULL && fast->next!=NULL)
        {
            slow=slow->next;
            fast=fast->next->next;
        }
        // return slow;
        temp1->next=slow->next;
        if (c==1){
            head=NULL
            ;
        }
        return head;
    }
};
