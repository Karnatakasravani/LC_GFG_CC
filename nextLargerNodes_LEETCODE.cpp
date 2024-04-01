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
    vector<int> nextLargerNodes(ListNode* head) {
        vector<int>v;
        while(head)
        {
            v.push_back(head->val);
            head=head->next;
        }
        reverse(v.begin(),v.end());
        vector<int>res;
        stack<int>s;
        for (int i=0;i<v.size();i++)
        {
            if (s.size()==0)
            {
                res.push_back(0);
            }
            else if (!s.empty() && v[i]<s.top())
            {
                res.push_back(s.top());
            }
            else{
                while(s.size()>0 && s.top()<=v[i])
                {
                    s.pop();
                }
                if(s.size()==0)
                {
                    res.push_back(0);
                }
                else{
                     res.push_back(s.top());
                }
            }
          s.push(v[i]);
        }
        reverse(res.begin(),res.end());
        return res;
        
        
    }
    
};
