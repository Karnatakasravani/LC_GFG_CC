class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        l=[]
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in d:
            if d[i]>1:
                l.append(i)
        return l
            
        
