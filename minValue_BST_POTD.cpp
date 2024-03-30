class Solution {
  public:
  int c=0;
    void leftmost(Node* root)
    {
        if(root==NULL)
        {
            return ;
        }
        else if(root->left==NULL and root!=NULL)
        {
            c=root->data;
            return ;
        }
        else
        {
            leftmost(root->left);
        }
        
    }
    int minValue(Node* root) {
        // Code here
        leftmost(root);
        if (c==0)
        {
            return -1;
        }
        else
        {return c;}
    }
};
