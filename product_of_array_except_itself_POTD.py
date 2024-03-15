class Solution:
    
    def productExceptSelf(self, a: List[int]) -> List[int]:
        n=len(a)
        left=[1]
        s=1
        for i in range(len(a)-1):
            s*=a[i]
            left.append(s)
        right=[1]
        p=1
        for j in range(len(a)-1,0,-1):
            p*=a[j]
            right.append(p)
        r=[]
        for i in range(len(right)-1,-1,-1):
            r.append(right[i])
        res=[1]*n
        l=a.count(0)
        for i in range(len(a)):
            if left[i]==r[i] and l==1:
                res[i]=left[i]
            else:
                res[i]=left[i]*r[i]
        return res
                

            
                
