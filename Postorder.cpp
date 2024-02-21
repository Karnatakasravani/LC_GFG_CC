class Solution {
public:
    void Postorder(TreeNode* root,vector<int>&v)
    {
        if(root==NULL){return ;}
        Postorder(root->left,v);
        Postorder(root->right,v);
        return v.push_back(root->val);
    }
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int>v;
        Postorder(root,v);
        return v;
        
    }
};
