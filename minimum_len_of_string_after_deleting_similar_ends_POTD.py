class Solution:
    def minimumLength(self, s: str) -> int:
        i=0
        j=len(s)-1
        if len(s)==3 and s[0]==s[2]:
            return 1
        if len(s)==1:
            return 1
        if s==s[::-1]:
            return 0
        if len(s)==2:
            if s[0]==s[1]:
                return 0
            else:
                return 2
        while(i<j):
            if s[i]==s[j] and s[i]!=s[i+1] and s[j]!=s[j-1] and j-i!=2:
                i+=1
                j-=1        
            elif s[i]==s[j] and s[i]==s[i+1] and s[j]!=s[j-1]:
                i+=1
            elif s[i]==s[j] and s[i]!=s[i+1] and s[j]==s[j-1]:
                j-=1
            elif s[i]==s[j] and s[i]==s[i+1] and s[j]==s[j-1] and j!=i+1 :
                i+=1
                j-=1
        #
            elif s[i]==s[j] and s[i]!=s[i+1] and s[j]!=s[j-1] and j-i==2:
                return (1)
                break
            else:
                if j-i==1 and s[i]==s[j]:
                    return 0
                return j-i+1
                break
