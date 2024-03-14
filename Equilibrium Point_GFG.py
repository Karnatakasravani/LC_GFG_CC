class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A, N):
        # Your code here
        s=0
        pre=[]
        if len(A)<3:
            return 1
        for i in range(0,N):
            s+=A[i]
            pre.append(s)
            # if pre[i-1]==pre[-1]-pre[i]:
            #     return i
        n=len(pre)
        for i in range(1,N):
            if pre[i-1]==pre[n-1]-pre[i]:
                return (i+1)
        else:
            return -1
