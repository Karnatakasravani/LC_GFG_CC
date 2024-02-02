#include<bits/stdc++.h>
using namespace std;
void fact(int n,int r)
{
	if (n==1) {
		cout<<r;
		return;
	}
	r*=n;
	fact(n-1,r);
}
int main()
{
   int n;
   cin>>n;
   fact(n,1);	
}
