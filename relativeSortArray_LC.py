class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d={}
        for i in arr1:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        a=[]
        for i in arr2:
            if i in arr1:
                for j in range(d[i]):
                    a.append(i)
        b=[]
        for i in arr1:
            if i not in a:
                b.append(i)
        b.sort()
        if len(b)==0:
            return a
        return a+b
