int flag=0;
int fun(Node* root,int x)
{
    // while(root)
    // {
        if(root==NULL)
        {
            return 0;
        }
        if(root->data==x)
        {
            flag=1;
            return 1;
        }
        else if(root->data>x)
        {
            fun(root->left,x);
        }
        else if(root->data<x)
        {
            fun(root->right,x);
        }
    // }
    
}
bool search(Node* root, int x) {
    // Your code here
    int res=fun(root,x);
    return res;
}
