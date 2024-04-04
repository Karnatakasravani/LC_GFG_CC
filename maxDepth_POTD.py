class Solution:
    def maxDepth(self, s: str) -> int:
        maxcou=0
        m=0
        for i in s:
            if i=="(":
                maxcou+=1
                m=max(m,maxcou)
            if i==")":
                maxcou-=1
            
        return m
        
