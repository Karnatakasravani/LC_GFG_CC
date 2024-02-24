class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        a=[]
        if n==1:
            return 1
        if n==2 and trust==[]:
            return -1
        for i in trust:
            for j in range(len(i)):
                    if(j==0):
                        a.append(i[j])
        k=list(set(a))
        s=sum(k)
        ns=n*(n+1)//2
        x=ns-s
        c=0
        s=[]
        for i in trust:
            for j in range(len(i)):
                if(j==1):
                    if(i[j]==x):
                        s.append(i[0])
        j=sum(s)
        m=ns-j
        if(m==x):
            return (x)
        else:
