#include<bits/stdc++.h>
using namespace std;
void solve(int close,int open,string s,int n )
{
	if (open+close>=2*n)
	{
		cout<<s<<endl;
		return;
	}
	if (close>open)return;
	
	if (open==n)
	{
		solve(close+1,open,s+')',n);
	}
	else{
		solve(close,open+1,s+'(',n);
		solve(close+1,open,s+')',n);
	}
}
int main()
{
    int n;
    cin>>n;
    solve(0,1,"(",n);
}
