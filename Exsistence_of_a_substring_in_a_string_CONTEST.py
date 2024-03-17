class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        l=[]
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if len(s[i:j+1])==2:
                    l.append(s[i:j+1])
        for i in l:
            if i in s[::-1]:
                return True
                break
        return False
        
        
