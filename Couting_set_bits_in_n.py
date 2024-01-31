class Solution:
    def countBits(self, n: int) -> List[int]:
        l=[]
        for i in range(0,n+1):
            c=0
            while(i!=0):
                c+=i&1
                i=i>>1
            l.append(c)
        return  l
        
