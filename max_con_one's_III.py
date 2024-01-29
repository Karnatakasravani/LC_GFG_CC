class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        m=0
        j=0
        for i in range(len(nums)):
            if nums[i]==0:
                k-=1
                while(k<0):
                    if nums[j]==0:
                   .     k+=1
                    j+=1
            m=max(m,i-j+1)
            
        return m
