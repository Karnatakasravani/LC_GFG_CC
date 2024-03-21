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
    ListNode* mergeInBetween(ListNode* list1, int a, int b, ListNode* list2) {
        ListNode* head=list1;
        int s=a;
        while(s>1){
            list1=list1->next;
            s--;
        }
        ListNode* k=list1->next;
        list1->next=list2;
        while(list1->next!=NULL){
            list1=list1->next;
        }
        while(b-a>=1){
            k=k->next;
            b--;
        }
        list1->next=k->next;
        return head;
    }
};
