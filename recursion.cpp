#include<bits/stdc++.h>
using  namespace std;
void table(int i,int n,int range)
{
	if (i>range) return ;
	cout<< n << " X " << i<<" = "<<n*i<<endl;
	table(i+1,n,range);
	
}
int main()
{
//	int n;
//	cin>>n;
//	int range;
//	cin>>range;
	table(1,2,20);
}
