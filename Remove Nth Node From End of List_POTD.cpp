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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int tot=0;
        ListNode* temp=head;
        while(temp)
        {
            tot+=1;
            temp=temp->next;
        }
       int p=tot-n;
    //    i=0;
       ListNode* temp1=head;
       ListNode* pre=NULL;
       if(p==0) return head->next;
       for( int i=0;i<p;i++)
       {
           pre=temp1;
           temp1=temp1->next;
       }
       pre->next=temp1->next;
       temp1=NULL;
        // cout<<p;
        return head;

        
    }
};
