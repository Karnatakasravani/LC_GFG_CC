class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        def encrypt(x):
            p=list(str(i))
            n=len(p)
            m=max(p)
            res=[m]*n
            return int("".join(res))    
        s=0
        for i in nums:
            s+=encrypt(i)
        return (s)
        
