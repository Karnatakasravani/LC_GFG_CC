class Solution:
    def pivotInteger(self, n: int) -> int:
        s=0
        pre=[]
        if n==1:
            return (1)
        if n<8 and n!=1:
            return (-1)
        for i in range(1,n+1):
            s+=i
            pre.append(s)
        N=len(pre)
        for i in range(1,n):
            if pre[i-1]==pre[N-1]-pre[i]:
                return (i+1)
        else:
            return -1
