#include<bits/stdc++.h>
using namespace std;
void reverse(int a[],int n,int i)
{
	if(i>=n){
		return;
	}
	reverse(a,n,i+1);
	cout<<a[i]<<" ";
}
int main()
{
	int a[]={1,2,3,4,5};
	reverse(a,5,0);
}
