/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
bool ans=true;
void Inorder(TreeNode* p,TreeNode* q)
{
    if (p==NULL && q!=NULL) ans=false;
    if(q==NULL && p!=NULL) ans=false;
    if(p==NULL) return ;
    if(q==NULL) return ;
    if(p->val!=q->val)
    {
        ans=false;
    } 
    Inorder(p->left,q->left);
    Inorder(p->right,q->right);
}
    bool isSameTree(TreeNode* p, TreeNode* q) {
        Inorder(p,q);
        return ans;
        
    }
};
