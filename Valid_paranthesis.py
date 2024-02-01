class Solution:
    
    #Function to check if brackets are balanced or not.
    def ispar(self,x):
        # code here
        l=[]
        d={'(': ')', '{': '}', '[' : ']'}
        if len(s)%2!=0:
            return False
        for i in x:
            if i in d:
                l.append(i)
            else:
                if l==[]:
                    return False
                a=l.pop()
                if i!=d[a]:
                    return False
        return l==[]
