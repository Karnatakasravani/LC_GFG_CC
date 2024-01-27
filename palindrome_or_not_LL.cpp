//{ Driver Code Starts
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <stack>
using namespace std;
/* Link list Node */
struct Node {
  int data;
  struct Node *next;
  Node(int x) {
    data = x;
    next = NULL;
  }
};




// } Driver Code Ends
/*
struct Node {
  int data;
  struct Node *next;
  Node(int x) {
    data = x;
    next = NULL;
  }
};
*/

class Solution{
  public:
    //Function to check whether the list is palindrome.
    bool isPalindrome(Node *head)
    {
        //Your code here
        Node* head1=NULL;
        Node* temp1=head1;
        Node* temp=head;
        while(temp)
        {
            int x=temp->data;
            Node* nn=new Node(x);
            nn->next=temp1;
            temp1=nn;
            temp=temp->next;
        }
        // Node* temp=head;
        int c=0;
        while(temp1!=NULL and head!=NULL)
        {
            if (temp1->data!=head->data)
            {
                return 0;
            // c++;
            }
            temp1=temp1->next;
            head=head->next;
        }
        return 1;
        // int c1=0;
        // while(head)
        // {
        //     head=head->next;
        //     c1+=1;
        // }
        // if (c1==c)
        // {
        //     return 1;
        // }
        // return (c1,c);
    }
};



//{ Driver Code Starts.
/* Driver program to test above function*/
int main()
{
  int T,i,n,l,firstdata;
    cin>>T;
    while(T--)
    {
        
        struct Node *head = NULL,  *tail = NULL;
        cin>>n;
        // taking first data of LL
        cin>>firstdata;
        head = new Node(firstdata);
        tail = head;
        // taking remaining data of LL
        for(i=1;i<n;i++)
        {
            cin>>l;
            tail->next = new Node(l);
            tail = tail->next;
        }
    Solution obj;
   	cout<<obj.isPalindrome(head)<<endl;
    }
    return 0;
}


// } Driver Code Ends
