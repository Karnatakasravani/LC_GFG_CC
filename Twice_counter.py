class Solution:
    def countWords(self,List, n):
        #code here
        d={}
        cnt=0
        for i in List:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in d:
            if d[i]==2:
                cnt+=1
        return cnt
