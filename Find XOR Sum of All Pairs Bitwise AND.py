class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        s1=0
        for i in arr1:
            s1^=i
        s2=0
        for j in arr2:
            s2^=j
        return s1&s2
        
