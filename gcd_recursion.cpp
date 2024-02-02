#include<bits/stdc++.h>
using namespace std;
void gcd(int a,int b)
{
	if(b==0){
		cout<<a;
		return;
	}
	gcd(b,a%b);
		
}
int main()
{
	int a,b;
	cin>>a>>b;
	if (a>b){
	   int t=a;
	   a=b;
	   b=t;
	}
	gcd(a,b);
}
