class Solution:
    def minSubArrayLen(self, k: int, n: List[int]) -> int:
        # n=[1,2,3,4,5]
        # n=[1,1,1,1,1,1,1,1]
        # k=11
        i=0
        j=0
        l=[]
        summ=0
        while(j<len(n)):
            summ+=n[j]#1
            while(summ>k):
                l.append(len(n[i:j+1]))
                summ-=n[i]
                i+=1
            if(summ==k):
                l.append(len(n[i:j+1]))
            j+=1
        if len(l)==0:
            return 0
        return min(l)
