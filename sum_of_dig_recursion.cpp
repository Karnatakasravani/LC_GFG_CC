#include<bits/stdc++.h>
using namespace std;
void sum_of_digit(int n,int i)
{
	if (n==0) {
		cout<<i;
		return ;
	}
	int d=n%10;
	i+=d;
	n=n/10;
	sum_of_digit(n,i);
	
}
int main()
{
	int n;
	cin>>n;
	sum_of_digit(n,0);
}
